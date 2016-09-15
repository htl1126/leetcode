import collections


class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
         @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.food = food[::-1]
        self.snake = collections.deque([[0, 0], ])
        self.dim = [height, width]
        self.score = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        dis = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}
        next_pos = [self.snake[-1][0] + dis[direction][0],
                    self.snake[-1][1] + dis[direction][1]]
        # Note that the next position could be the tail of the snake
        if not (0 <= next_pos[0] < self.dim[0] and
                0 <= next_pos[1] < self.dim[1]) or \
                next_pos in self.snake and next_pos != self.snake[0]:
            return -1
        if self.food and [next_pos[0], next_pos[1]] == self.food[-1]:
            self.snake.append([self.food[-1][0], self.food[-1][1]])
            self.food.pop()
            self.score += 1
        else:
            self.snake.append([next_pos[0], next_pos[1]])
            self.snake.popleft()
        return self.score


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
