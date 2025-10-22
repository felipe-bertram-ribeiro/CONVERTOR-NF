from lxml import etree
from pathlib import Path
from .utils import safe_text, safe_float

NF_NAMESPACE = '{http://www.portalfiscal.inf.br/nfe}'

def parse_nfe_xml(path: Path) -> dict:
    """Lê XML de NF-e e retorna dicionário com dados principais e produtos."""
    try:
        tree = etree.parse(str(path))
        root = tree.getroot()
    except Exception as e:
        raise RuntimeError(f'Erro ao ler XML {path.name}: {e}')

    infnfe = root.find('.//' + NF_NAMESPACE + 'infNFe') or root.find('.//infNFe') or root.find('.//{*}infNFe')
    chave = None
    if infnfe is not None and 'Id' in infnfe.attrib:
        chave = infnfe.attrib.get('Id').replace('NFe', '')

    # Emitente
    emit = root.find('.//' + NF_NAMESPACE + 'emit') or root.find('.//emit') or root.find('.//{*}emit')
    emit_cnpj = safe_text(emit.find(NF_NAMESPACE + 'CNPJ') if emit is not None else None) or safe_text(emit.find('CNPJ') if emit is not None else None)
    emit_xnome = safe_text(emit.find(NF_NAMESPACE + 'xNome') if emit is not None else None) or safe_text(emit.find('xNome') if emit is not None else None)

    # Destinatário
    dest = root.find('.//' + NF_NAMESPACE + 'dest') or root.find('.//dest') or root.find('.//{*}dest')
    dest_cnpj = (safe_text(dest.find(NF_NAMESPACE + 'CNPJ') if dest is not None else None)
                 or safe_text(dest.find('CNPJ') if dest is not None else None)
                 or safe_text(dest.find(NF_NAMESPACE + 'CPF') if dest is not None else None)
                 or safe_text(dest.find('CPF') if dest is not None else None))
    dest_xnome = safe_text(dest.find(NF_NAMESPACE + 'xNome') if dest is not None else None) or safe_text(dest.find('xNome') if dest is not None else None)

    # Data de emissão
    ide = root.find('.//' + NF_NAMESPACE + 'ide') or root.find('.//ide') or root.find('.//{*}ide')
    data_emissao = None
    if ide is not None:
        de = ide.find(NF_NAMESPACE + 'dEmi') or ide.find('dEmi')
        dhe = ide.find(NF_NAMESPACE + 'dhEmi') or ide.find('dhEmi')
        data_emissao = safe_text(dhe) or safe_text(de)

    # Totais
    icmstot = root.find('.//' + NF_NAMESPACE + 'ICMSTot') or root.find('.//ICMSTot') or root.find('.//{*}ICMSTot')
    valor_total = None
    if icmstot is not None:
        valor_total = safe_text(icmstot.find(NF_NAMESPACE + 'vNF') or icmstot.find('vNF'))

    # Produtos
    produtos = []
    det_nodes = root.findall('.//' + NF_NAMESPACE + 'det') or root.findall('.//det') or root.findall('.//{*}det')
    for det in det_nodes:
        prod = det.find(NF_NAMESPACE + 'prod') or det.find('prod') or det.find('.//{*}prod')
        if prod is None:
            continue
        descricao = safe_text(prod.find(NF_NAMESPACE + 'xProd') or prod.find('xProd'))
        qcom = safe_text(prod.find(NF_NAMESPACE + 'qCom') or prod.find('qCom'))
        vunit = safe_text(prod.find(NF_NAMESPACE + 'vUnCom') or prod.find('vUnCom'))
        vprod = safe_text(prod.find(NF_NAMESPACE + 'vProd') or prod.find('vProd'))
        produtos.append({
            'descricao': descricao,
            'quantidade': safe_float(qcom),
            'valor_unitario': safe_float(vunit),
            'valor_total_item': safe_float(vprod),
        })

    total_itens = sum([p['quantidade'] for p in produtos if p['quantidade'] is not None]) if produtos else None

    return {
        'arquivo': path.name,
        'chave': chave,
        'emit_cnpj': emit_cnpj,
        'emit_xnome': emit_xnome,
        'dest_cnpj': dest_cnpj,
        'dest_xnome': dest_xnome,
        'data_emissao': data_emissao,
        'valor_total': safe_float(valor_total),
        'total_itens': total_itens,
        'produtos': produtos,
    }

def read_folder(folder_path: str, update_progress=None) -> list:
    """Lê todos os arquivos XML da pasta e retorna lista de notas; grava logs de erro."""
    p = Path(folder_path)
    notas = []
    xml_files = list(sorted(p.glob('*.xml')))
    for idx, f in enumerate(xml_files, 1):
        try:
            nota = parse_nfe_xml(f)
            notas.append(nota)
        except Exception as e:
            with open('logs.txt', 'a', encoding='utf-8') as log:
                log.write(f'{f.name}: {e}\n')
        if update_progress:
            update_progress(idx, len(xml_files))
    return notas
