import CaboCha

def parse_cabocha(input_file_name, output_file_name):
    """
    プレーンな日本語の文章ファイルを係り受け解析してファイルに保存する.
    (空白は削除します.)
    :param input_file_name プレーンな日本語の文章ファイル名
    :param output_file_name 係り受け解析済みの文章ファイル名
    """
    c = CaboCha.Parser()
    with open(input_file_name, encoding='utf-8') as f:
        with open(output_file_name, mode='w', encoding='utf-8') as output_file:
            for line in f:
                tree = c.parse(line.lstrip())
                output_file.write(tree.toString(CaboCha.FORMAT_LATTICE))


parse_cabocha('neko.txt', 'neko.txt.cabocha')
