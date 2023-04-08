import copy
import random


class Hat:

  def __init__(self, **balls):
    self.contents = []
    for ball, count in balls.items():
      self.contents += [ball] * count

  def draw(self, num_balls):
    if num_balls >= len(self.contents):
      balls_drawn = self.contents
      self.contents = []
    else:
      balls_drawn = random.sample(self.contents, num_balls)
      for ball in balls_drawn:
        self.contents.remove(ball)
    return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  num_successful = 0
  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)
    expected_balls_copy = copy.deepcopy(expected_balls)
    for ball in balls_drawn:
      if ball in expected_balls_copy:
        expected_balls_copy[ball] -= 1
    if all(count <= 0 for count in expected_balls_copy.values()):
      num_successful += 1
  return num_successful / num_experiments
