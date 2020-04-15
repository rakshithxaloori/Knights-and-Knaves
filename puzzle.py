from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
AClaim = And(AKnave, AKnight)
knowledge0 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    Implication(AKnave, Not(AClaim)),
    Implication(AKnight, AClaim)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
AClaim = And(AKnave, BKnave)
knowledge1 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Implication(AKnave, Not(AClaim)),
    Implication(AKnight, AClaim)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
AClaim = Or(And(AKnave, BKnave), And(AKnight, BKnight))
BClaim = Or(And(AKnave, BKnight), And(AKnight, BKnave))
knowledge2 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    Implication(AKnave, Not(AClaim)),
    Implication(AKnight, AClaim),
    Implication(BKnave, Not(BClaim)),
    Implication(BKnight, BClaim)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
AClaim1 = AKnight
AClaim2 = AKnave
BClaim = And(AClaim2, CKnave)
CClaim = AKnight
knowledge3 = And(
    And(Or(AKnave, AKnight), Not(And(AKnave, AKnight))),
    And(Or(BKnave, BKnight), Not(And(BKnave, BKnight))),
    And(Or(CKnave, CKnight), Not(And(CKnave, CKnight))),

    Implication(AKnave, Not(Or(AClaim1, AClaim2))),
    Implication(AKnight, Or(AClaim1, AClaim2)),

    Implication(BKnave, Not(BClaim)),
    Implication(BKnight, BClaim),

    Implication(CKnave, Not(CClaim)),
    Implication(CKnight, CClaim)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
