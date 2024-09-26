import svgwrite

def create_svg(data):
    dwg = svgwrite.Drawing('example.svg', profile='tiny')

    for level_index, level in enumerate(data):
        group = dwg.add(dwg.g(id=f'level-{level_index}',
                              transform=f'translate(0, {level_index * 150})'))  # increased margin to 150px

        for pair_index, pair in enumerate(level):

            rect_width = 80
            rect_height = 50

            # Divide each rectangle in half
            rect1 = group.add(dwg.rect(
                insert=(pair_index * 100 + 20, 0),  # increased margin to 100px and added 20px margin
                size=(rect_width / 2, rect_height),
                fill='lightgray' if pair[0] == min(x[0] for x in level) else 'none',
                # set fill to lightgray if pair is min, else none
                stroke='black'
            ))

            rect2 = group.add(dwg.rect(
                insert=(pair_index * 100 + 20 + rect_width / 2, 0),
                size=(rect_width / 2, rect_height),
                fill='lightgray' if pair[0] == min(x[0] for x in level) else 'none',
                stroke='black'
            ))

            text1 = group.add(dwg.text(
                f'{pair[0]}',
                insert=(pair_index * 100 + 30, 25)
            ))
            text2 = group.add(dwg.text(
                f'{pair[1]}',
                insert=(pair_index * 100 + 60, 25)
            ))

    dwg.save()