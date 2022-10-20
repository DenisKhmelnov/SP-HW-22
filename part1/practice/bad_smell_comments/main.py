
class Unit:
    def move(self, field, coord_x: int, coord_y: int, direction: str, is_flight: bool, is_crawl: bool, basic_speed = 1):

        if is_flight and is_crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_flight:
            basic_speed *= 1.2
            if direction == 'UP':
                new_y = coord_y + basic_speed
                new_x = coord_x
            elif direction == 'DOWN':
                new_y = coord_y - basic_speed
                new_x = coord_x
            elif direction == 'LEFT':
                new_y = coord_y
                new_x = coord_x - basic_speed
            elif direction == 'RIGHT':
                new_y = coord_y
                new_x = coord_x + basic_speed
        if is_crawl:
            basic_speed *= 0.5
            if direction == 'UP':
                new_y = coord_y + basic_speed
                new_x = coord_x
            elif direction == 'DOWN':
                new_y = coord_y - basic_speed
                new_x = coord_x
            elif direction == 'LEFT':
                new_y = coord_y
                new_x = coord_x - basic_speed
            elif direction == 'RIGHT':
                new_y = coord_y
                new_x = coord_x + basic_speed

            field.set_unit(x=new_x, y=new_y, unit=self)
