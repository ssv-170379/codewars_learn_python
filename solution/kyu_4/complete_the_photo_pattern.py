"""
Complete the photo pattern
https://www.codewars.com/kata/58477f76ad2567b465000153
"""
"""
    When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said

In this kata, No algorithms, only funny ;-)
Description:

"All the people hurry up! We need to take a picture. The tallest standing in the middle, and then left and right descending...All the people, hand in hand..."

Give you an array legs. It recorded the length of the legs of all the people(we assume that their upper body is the same height), please follow the above rules to arrange these people, and then complete and return the photo:

legs = [1,2,3]
After arrange --> [2,3,1]

The photo should be:
             + +   
   + +      +o o+  
  +o o+    +  u  +      + +     
 +  u  +    + ~ +      +o o+  
  + ~ +       |       +  u  + 
    |       +-o-+      + ~ +  
  +-o-+    /| o |\       |    
_/| o |\__/ +-o-+ \    +-o-+  
  +-o-+      | |   \__/| o |\_
   | |       | |       +-o-+  
   I I       I I        I I   
 
 
 
legs = [1,1,1,2,3]
After arrange --> [1,2,3,1,1]

The photo should be:
                       + +   
             + +      +o o+  
   + +      +o o+    +  u  +      + +      + +     
  +o o+    +  u  +    + ~ +      +o o+    +o o+  
 +  u  +    + ~ +       |       +  u  +  +  u  + 
  + ~ +       |       +-o-+      + ~ +    + ~ +  
    |       +-o-+    /| o |\       |        |    
  +-o-+    /| o |\__/ +-o-+ \    +-o-+    +-o-+  
_/| o |\__/ +-o-+      | |   \__/| o |\__/| o |\_
  +-o-+      | |       | |       +-o-+    +-o-+  
   I I       I I       I I        I I      I I   
 
 

Note:

    The length of array legs always be a positive odd integer, all elements are positive integers.
    The order is tallest in the middle, then left, then right, then left, then right..
    If necessary, please add some spaces on both sides.
    Please pay attention to "hand in hand". You can assume that their arms are retractable ;-)
"""


def pattern(legs: list[int]) -> str:
    def sort_by_height(legs: list) -> list:
        """The tallest standing in the middle, and then left and right descending"""
        descend = list(reversed(sorted(legs)))  # tallest first
        sorted_ = []
        sides = ['right', 'left'] * (len(descend) // 2 + 1)  # ['left', 'right', 'left', 'right'...] repeated for no shorter than quantity of persons
        for height, side, in zip(descend, sides):
            if side == 'right':
                sorted_.append(height)
            else:  # side == 'left'
                sorted_.insert(0, height)
        return sorted_

    def calculate_arms_length(legs: list) -> list[dict]:
        """All the people, hand in hand. You can assume that their arms are retractable"""
        persons_descr = []
        for i in range(len(legs)):

            arm_left = 1  # default length
            if i > 0 and legs[i] > legs[i - 1]:  # if person on the left side is lower - extend left arm
                arm_left = legs[i] - legs[i - 1] + 1

            arm_right = 1  # default length
            if i < len(legs) - 1 and legs[i] > legs[i + 1]:  # if person on the right side is lower - extend right arm
                arm_right = legs[i] - legs[i + 1] + 1

            persons_descr.append({'arm_left': arm_left, 'arm_right': arm_right, 'legs': legs[i]})
        return persons_descr

    def photo_person(person_descr: dict, photo_height: int) -> list:
        """Get an ascii-drawing of a person based on their legs and arms lengths"""
        arm_left, arm_right, legs = person_descr['arm_left'], person_descr['arm_right'], person_descr['legs']
        legs_extend_index = 8  # extend legs from this vertical position
        arms_extend_index = 7  # extend arms from this vertical position
        left_palm_index = arms_extend_index + arm_left - 2  # left palm vertical_position
        right_palm_index = arms_extend_index + arm_right - 2  # right palm vertical_position

        person = [
            '  + +  ',
            ' +o o+ ',
            '+  u  +',
            ' + ~ + ',
            '   |   ',
            ' +-o-+ ',
            '/| o |\\',
            ' +-o-+ ',
            '  I I  ',
        ]

        # extend legs, if longer than 1
        for i in range(legs - 1):
            person.insert(legs_extend_index, '  | |  ')

        def str_replace_character_at_index(string, index, character):
            if index < 0:  # convert negative to absolute index
                index = len(string) + index
            return string[:index] + character + string[index + 1:]

        # draw arms
        for i, line in enumerate(person):
            line = (' ' * arm_left) + line + (' ' * arm_right)  # add horizontal space for arms and palms

            if i >= arms_extend_index and i <= left_palm_index:  # retract left arm if palm is lower than extend_index
                line = str_replace_character_at_index(line, 1 + (left_palm_index - i), '/')
            if i >= arms_extend_index and i <= right_palm_index:  # retract right arm if palm is lower than extend_index
                line = str_replace_character_at_index(line, -2 - (right_palm_index - i), '\\')

            if i == left_palm_index:  # draw left palm
                line = str_replace_character_at_index(line, 0, '_')
            if i == right_palm_index:  # draw right palm
                line = str_replace_character_at_index(line, -1, '_')
            person[i] = line

        space_above_head = [' ' * len(person[0]) for _ in range(photo_height - len(person))]
        person = space_above_head + person  # draw some space above the person's head is they are lower than photo height

        return person

    def compose_group_photo(individual_photos: list[list[str]]) -> list[str]:
        """combine individual photos side-by-side to get the full picture"""
        photo_height = len(individual_photos[0])  # all the photos are of the same height, so we may pick any to sample
        photo = []
        for scanline in range(photo_height):
            line = ''.join([ph[scanline] for ph in individual_photos])
            photo.append(line)
        return photo

    persons_sorted = sort_by_height(legs)  # tallest in the middle, then left, then right, then left, then right..
    persons_descr = calculate_arms_length(persons_sorted)  # add information about arms length to match arms for 'hand in hand' pose

    photo_height = max(p + 8 for p in legs)  # height of the photo corresponds with the height of the tallest person,
    individual_photos = [photo_person(p, photo_height) for p in persons_descr]  # take individual pictures of each person

    photo = compose_group_photo(individual_photos)  # stitch individual photos side-by-side

    return '\n'.join(photo)
