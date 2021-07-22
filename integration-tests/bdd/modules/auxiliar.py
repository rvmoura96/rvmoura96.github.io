from ast import literal_eval


def convert_from_table_to_schema(table_value):
    """
    Converte os nomes em português nas tabelas para o schema do request.
    """
    relations = {
        "categoria": "ec",
        "ação": "ea",
        "rótulo": "el",
        "tipo": "t",
    }
    try:
        return relations[table_value]
    except KeyError:
        return table_value


def convert_string_to_object(value):
    """Converte uma string em objeto."""
    try:
        return literal_eval(value)
    except ValueError:
        return value


def parse_behave_table(context_table):
    """Faz o cast da tabela do behave em um dicionário."""
    return next(
        dict(zip(context_table.headings, row)) for row in context_table.rows
    )


def cast_table_to_dict(context_table):
    """Convete as tableas do behave em dicionários com tipos."""
    dict_with_strings = parse_behave_table(context_table)
    return {
        convert_from_table_to_schema(key): convert_string_to_object(value)
        for key, value in dict_with_strings.items()
    }


def cast_table_with_one_column_to_list(context_table):
    """Converte uma tabela com somente uma coluna em uma lista."""
    assert len(context_table.headings), "Tabela com mais de uma coluna"
    return [row[context_table.headings[0]] for row in context_table]
