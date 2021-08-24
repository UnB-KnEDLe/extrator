"""Regras regex para ato de Contrato."""

import re
import os
import joblib
from dodfminer.extract.polished.acts.base import Atos


class Contracts(Atos):

    def __init__(self, file, backend):
        super().__init__(file, backend)

    def _regex_flags(self):
        return re.IGNORECASE

    # def _load_model(self):
    #     f_path = os.path.dirname(__file__)
    #     f_path += '/models/aposentadoria.pkl'
    #     return joblib.load(f_path)

    def _act_name(self):
        return "Contrato"

    def _props_names(self):
        return ["Tipo do Ato", "Contrato", "Processo", "Data de Assinatura", "Partes", "Objeto", "Vigencia",
                "Valor", "Unidade de Orçamento", "Programa de Trabalho", "Natureza da Despesa", "Nota de Empenho", "Número do Ajuste",
                "Orgão Contratante", "Entidade Contratada", "Entidade Convenente"]

    def _rule_for_inst(self):
        start = r"(EXTRATO\sD[O|E]\sCONTRATO)"
        body = r"([.|\s|\S]*?)"
        end = r"<>END OF BLOCK<>"
        return start + body + end

    def _prop_rules(self):
        rules = {
            'contrato': '(\d+/\d{4})', # OK -----
            'processo': '[P|p][R|r][O|o][C|c][E|e][S|s][S|s][O|o][:|\sSEI].*?(\d+[\.|-|-|\/]\d+[\.|-|-|\/]\d+[\.|-|-|\/]\d*)', #OK -----
            'data_assinatura': '[A|a][S|s][S|s][I|i][N|n][A|a][T|t][U|u][R|r][A|a]:\s(\d{2}\/\d{2}\/\d{4})', #OK -----
            'partes': '[P|p][A|a][R|r][T|t][E|e][S|s]:([^.]*)', #OK ANALISAR
            'objeto': '[O|o][B|b][J|j][E|e][T|t][O|o]:([^.]*)', #OK ANALISAR
            'vigencia': '[V|v][I|i][G|g][E|e][N|n][C|c][I|i][A|a]:[\S\s]([^.]*)', #OK ANALISAR
            'valor': '[v|V][a|A][l|L][o|O][r|R].*?[c|C][o|O][n|N][t|T][r|R][a|A][t|T][o|O][\S\s]*?([\d\.]*,\d{2})', #OK -----
            'unidade_orcamento': '[o|O][r|R][c|C][a|A][m|M][e|E][n|N][t|T][a|A][r|R][i|I][a|A].*?(\d+.\d+)', #OK -----
            'programa_trabalho': 'Programa de Trabalho[:|;][\s\S].*?(\d*.\d*.\d*.\d*.\d{4,6})', #OK -----
            'natureza_emepnho': 'Natureza d[e|a] Despesa:[\s\S].*?([\d.\d]*)', #OK -----
            'nota_empenho': '(\d+NE\d+)', #OK -----
            'numero_ajuste': 'Numero do ajuste: ([^;]*)', # ntem
            'orgao_contratante': 'Órgão contratante: ([^;]*)',# ntem
            'entidade_contratada': '[c|C][o|O][n|N][t|T][r|R][a|A][t|T][a|A][d|D][a|A|o|O].(.+\w+[\s\S].*?[\/.|])', #OK ANALISAR
            'entidade_convenente': 'Entidades convenentes: ([^;]*)' #ntem
        }
        return rules

            # 'contrato': '[c|C][o|O][n|N][t|T][r|R][a|A][t|T][o|O](:|)\s([n|N]).\s(\d+\/\d{4})', #ok
            # 'processo': '[P|p][R|r][O|o][C|c][E|e][S|s][S|s][O|o][:|\sSEI].*?(\d+[\.|-|-|\/]\d+[\.|-|-|\/]\d+[\.|-|-|\/]\d*)', #ok
            # 'data_assinatura': '[A|a][S|s][S|s][I|i][N|n][A|a][T|t][U|u][R|r][A|a]:\s(\d{2}\/\d{2}\/\d{4})',
            # 'partes': '[P|p][A|a][R|r][T|t][E|e][S|s]:([^.]*)', #ok
            # 'objeto': '[O|o][B|b][J|j][E|e][T|t][O|o]:([^.]*)', #ok
            # 'vigencia': '[V|v][I|i][G|g][E|e][N|n][C|c][I|i][A|a]:[\S\s]([^.]*)', #ok
            # 'valor': '[v|V][a|A][l|L][o|O][r|R]([:]|[\s\S]|[t|T][o|O][t|T][a|A][l|L]|[e|E][s|S][t|T][i|I][m|M][a|A][d|D][o|O]|[a|A][t|T][u|U][a|A][l|L]|[a|A][n|N][u|U][a|A][l|L]|[d|D][e|E|o|O]).*?([c|C][o|O][n|N][t|T][r|R][a|A][t|T][o|O]).*?(\d,\d{2})', #ok
            # 'unidade_orcamento': '([u|U][n|N][i|I][d|D][a|A][d|D][eE|])(.|\S|\s)([o|O][r|R][c|C][a|A][m|M][e|E][n|N][t|T][a|A][r|R][i|I][a|A])(.|\S|\s)(.|\S|\s)\d*', #ok
            # 'programa_trabalho': 'Programa de Trabalho[:|;][\s\S].*?\d*.\d*.\d*.\d*.\d{4}', #ok
            # 'natureza_emepnho': 'Natureza d[e|a] Despesa:[\s\S]([^;|^\s]*)',
            # 'nota_empenho': '[n|N][o|O][t|T][a|A][\s|\S][d|D][e|E][\s|\S][e|E][m|M][p|P][e|E][n|N][h|H][o|O].*(\d)',
            # 'numero_ajuste': 'Número do ajuste: ([^;]*)',
            # 'orgao_contratante': 'Órgão contratante: ([^;]*)',
            # 'entidade_contratada': 'Entidade contratada: ([^;]*)',
            # 'entidade_convenente': 'Entidades convenentes: ([^;]*)'