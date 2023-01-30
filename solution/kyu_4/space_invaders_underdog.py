"""
Space Invaders Underdog
https://www.codewars.com/kata/59fabc2406d5b638f200004a
"""
"""
This kata is inspired by Space Invaders (Japanese: スペースインベーダー), an arcade video game created by Tomohiro Nishikado and released in 1978.

Alien invaders are attacking Earth and you've been conscripted to defend.
The Bad News: You performed poorly in the manual training. As a result, you're ranked low priority and you're piloting a space jalopy.
The Good News: Your coding skill is better than your piloting and you know the movement pattern of the alien spaceships.

You're going to program an algorithm that aids in shooting down the incoming alien wave despite your limitations.
Input

The action takes place on an m x n matrix. Your function will receive two arguments:

    a 2-D array where each subarray represents a row of alien ships. Subarrays consist of integers that represent each alien ship. Zero values (0) are empty spaces.
    your [row,column] coordinates

The width (n) of a row is equal to the length of a subarray in the first argument and all rows are of the same length.
Your row coordinate will be the last row of the matrix (m - 1).

Alien Ship Movement Pattern

    Each alien ship is given in the form of an integer that represents its movement speed and direction.
    Alien ships move left or right. A positive integer means an alien moves right, a negative integer means an alien moves left. The absolute value of the integer is the distance the alien moves in 1 turn.
    When an alien reaches an edge, it moves down one position and reverses lateral (left/right) direction.

Your Ship's Limitations

    Your position is fixed.
    Your pulse cannon has a time delay of 1 turn. After the delay, your cannon blasts the first target in its path.
    You can fire up to one shot per turn.

Output

Your function should return an array of integers. Each integer represents the turn for each shot fired from your ship's cannon. If it is not possible to destroy all alien ships before they reach the last row, return null or None.

Test Example
https://i.imgur.com/S4qYQQ0.png Turn 0 (Initial State)
https://i.imgur.com/Iah7dQc.png Turn 1

The images above represent the matrix states at Turn 0 and Turn 1 for the test example below. Note the following:

    Multiple alien ships can occupy the same space concurrently. The red alien at [0,2] and the light blue alien at [0,7] at turn 0 will both end up at position [0,4] at turn 1.
    The pink alien (1) at [0,9] at turn 0 is already at the right edge, so it moves one space down and changes direction from right to left.
    The yellow alien (6) at [0,6] at turn 0 ends up at [1,7] at turn 1.
    The green alien (7) at [0,8] at turn 0 ends up at [1,4] (white alien) and gets shot down by your cannon at turn 1. Therefore, the time of registering your first shot is at turn 0.

In the test example, there is only one subarray in the first argument, meaning only the top row (row 0) of the matrix is occupied at the initial state.

alien_wave = [[3,1,2,-2,2,3,6,-3,7,1]]
position = [6,4]

blast_sequence(alien_wave,position)# [0, 2, 3, 4, 5, 9, 10, 13, 19, 22]

Other Technical Details

    In the event where multiple alien ships occupy the same position and the position is the target of your cannon fire, the fastest alien ship will be destroyed. If two ships are going at the same speed in opposite directions, the ship moving to the right will be destroyed.
    All alien ship movement speeds will be less than the width of the matrix.
    Alien count upper bound is 228
    Inputs will always be valid

If you enjoyed this kata, be sure to check out my other katas https://www.codewars.com/users/docgunthrop/authored.
"""

from dataclasses import dataclass

@dataclass
class YX:
    y: int
    x: int


class AlienSpaceShip:
    def __init__(self, position: YX, speed: int):
        self.position = position
        self.speed = speed

    def move(self, field_dimensions):
        self.position.x += self.speed  # move horizontally

        if self.position.x < 0:  # if outside left boundary
            self.position.x = (self.position.x + 1) * -1  # rebound horizontal position
            self.position.y += 1  # descend one line
            self.speed *= -1  # switch direction

        elif self.position.x >= field_dimensions.x:  # if outside right boundary
            self.position.x = field_dimensions.x - 1 - (self.position.x - field_dimensions.x)  # rebound horizontal position
            self.position.y += 1  # descend one line
            self.speed *= -1  # switch direction


class PlayerSpaceShip:
    def __init__(self, position: YX):
        self.position = position
        self.cannon_log = []  # log turn number when cannon fired

    def aim(self, aliens: list[AlienSpaceShip]) -> AlienSpaceShip | None:
        """Return: Closest and fastest target on the line of fire (prefer ones moving in right direction). Return: None (if no targets found)"""
        targets = [alien for alien in aliens if alien.position.x == self.position.x]  # targets on the line of fire

        if not targets:  # no target found
            return

        if len(targets) > 1:  # multiple targets found, narrow down search
            targets = [alien for alien in targets if alien.position.y == max(alien.position.y for alien in targets)]  # pick lowest targets (closest to the pilot)
            if len(targets) > 1:  # multiple targets found, narrow down search
                targets = sorted(targets, key=lambda alien: (abs(alien.speed), alien.speed), reverse=True)  # prioritize fastest speed. if multiple fastest targets, prefer positive value (moving right).

        return targets[0]  # target found

    def fire_cannon(self, aliens: list[AlienSpaceShip], target: AlienSpaceShip, current_turn: int):
        """Remove target from aliens (i.e. destroy target), log current turn number"""
        aliens.remove(target)
        self.cannon_log.append(current_turn)


class Invaders:
    def __init__(self, aliens: list[AlienSpaceShip], player: PlayerSpaceShip, field_dimensions: YX):
        self.aliens = aliens
        self.player = player
        self.field_dimensions = field_dimensions  # height and width of the game field
        self.turn = 0  # count game turns
        self.state = 'in_progress'  # game status: 'in_progress' | 'lose' | 'win'

    def play(self) -> list[int] | None:
        while self.state == 'in_progress':
            for alien in self.aliens:  # all aliens
                alien.move(self.field_dimensions)  # move
            target = self.player.aim(self.aliens)  # search for eligible alien ship to destroy
            if target:
                self.player.fire_cannon(self.aliens, target, self.turn)  # shot target
            self.turn += 1  # next turn
            self.update_status()

        if self.state == 'win':
            return self.player.cannon_log
        elif self.state == 'lose':  # "Explicit is better than implicit."
            return None

    def update_status(self):
        """Check win/lose criteria"""
        if not self.aliens:  # no aliens left
            self.state = 'win'
        elif max(alien.position.y for alien in self.aliens) == self.field_dimensions.y - 1:  # aliens reached the last row
            self.state = 'lose'


def blast_sequence(aliens: list[list[int]], pilot_position: list[int]) -> list[int] | None:
    aliens_parsed = []
    for y in range(len(aliens)):
        for x in range(len(aliens[y])):
            if aliens[y][x] != 0:  # 0 - empty position in wave
                aliens_parsed.append(AlienSpaceShip(position=YX(y, x), speed=aliens[y][x]))  # create alien ship and add to the list

    field_dimensions = YX(pilot_position[0] + 1, len(aliens[0]))  # game field: height - pilot.y + 1, width = width of alien wave
    player = PlayerSpaceShip(YX(*pilot_position))

    game = Invaders(aliens_parsed, player, field_dimensions)
    return game.play()
