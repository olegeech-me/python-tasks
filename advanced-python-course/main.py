import turtle as t

class LSystem:
    '''Simple class for L-System simulations'''

    def __init__(self, axiom, rule, length, angle):
        self.axiom = axiom
        self.rule = rule
        self.length = length
        self.angle = angle

    def draw(self, no_of_iters):
        current = self.axiom
        ruleset = self.rule.split('->')
        while no_of_iters > 1:
            current = current.replace(ruleset[0], ruleset[1])
            no_of_iters -= 1
        print('I will draw this:',current)

        t.color('red', 'blue')
        t.speed(2)

        for symbol in current:
            match symbol:
                case 'F':
                    t.forward(self.length)
                case '+':
                    t.right(self.angle)
                case '-':
                    t.left(self.angle)

        input('Press any key to finish the program')


koch = LSystem('F++F++F', 'F->F-F++F-F', 40, 60)
koch.draw(4)



