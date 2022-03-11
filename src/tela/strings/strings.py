def montar_organizador_string(organizadores: list):
    orgString = ''
    if len(organizadores) == 0:
        orgString = 'Nenhum organizador inserido'
    else:
        for organizador in organizadores:
            if organizador.cpf == organizadores[-1].cpf:
                orgString += organizador.nome
            else:
                orgString += organizador.nome + ', '

    return orgString


def montar_participante_string(participantes: list):
    partString = ''
    if len(participantes) == 0:
        partString = 'Nenhum participante inserido'
    else:
        for participante in participantes:
            if participante.cpf == participantes[-1].cpf:
                partString += participante.nome
            else:
                partString += participante.nome + ', '

    return partString


def montar_participacao_string(participacoes: list):
    pcaoString = ''
    if len(participacoes) == 0:
        pcaoString = 'Nenhuma participação inserida'
    else:
        for participacao in participacoes:
            if participacao.id == participacoes[-1].id:
                pcaoString += participacao.participante.nome
            else:
                pcaoString += participacao.participante.nome + ', '

    return pcaoString
