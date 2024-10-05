import svgwrite

def create_svg(data):
    dwg = svgwrite.Drawing('tree.svg', profile='tiny', size=(300, 450),
                            )

    for level_index, level in enumerate(data):
        group = dwg.add(dwg.g(id=f'level-{level_index}',
                              transform=f'translate(0, {level_index * 75})'))

        for pair_index, pair in enumerate(level):
            rect_width = 80
            rect_height = 40

            # Divide each rectangle in half
            rect1 = group.add(dwg.rect(
                insert=(pair_index * 100 + 20, 0),
                size=(rect_width / 2, rect_height),
                fill='#CCCCCC' if pair[0] == min(x[0] for x in level) else 'none',
                stroke='black'
            ))

            rect2 = group.add(dwg.rect(
                insert=(pair_index * 100 + 20 + rect_width / 2, 0),
                size=(rect_width / 2, rect_height),
                fill='#CCCCCC' if pair[0] == min(x[0] for x in level) else 'none',
                stroke='black'
            ))

            text1 = group.add(dwg.text(
                f'{pair[0]}',
                insert=(pair_index * 100 + 25, 25)
            ))
            text2 = group.add(dwg.text(
                f'{pair[1]}',
                insert=(pair_index * 100 + 65, 25)
            ))


    dwg.save()

def create_node_solution(solution_dict):
    dwg = svgwrite.Drawing(filename='node_solution.svg', profile='tiny',size=(200, 200),
                           )
    dwg.add(dwg.text('Задача', insert=(15, 35), fill='black'))
    dwg.add(dwg.text('-', insert=(45, 35), fill='black'))
    dwg.add(dwg.text('Узел', insert=(50, 35), fill='black'))

    for key, value in solution_dict.items():
        group = dwg.add(dwg.g(id=f'level-{key}',
                              transform=f'translate(0, {key * 25})'))
        text1 = group.add(dwg.text(
            f'{key}',
            insert=(30, 25)
        ))
        text2 = group.add(dwg.text(
            '-',
            insert = (45,25)
        ))
        text3 = group.add(dwg.text(
            f'{value}',
            insert=(60, 25)
        ))
    dwg.save()

def create_combine_solution():
    dwg = svgwrite.Drawing('combined_image.svg', profile='tiny',size=(900, 600))
    image1 = dwg.add(dwg.image('tree.svg', insert=(0, 0), size=(300, 450)))
    image2 = dwg.add(dwg.image('node_solution.svg', insert=(350, 0), size=(300, 500)))
    dwg.save()