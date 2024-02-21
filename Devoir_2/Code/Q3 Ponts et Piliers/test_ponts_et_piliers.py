# CE FICHIER NE SERT QU'A APPELER ET TESTER VOTRE CODE.
# VOUS NE DEVRIEZ PAS AVOIR BESOIN DE LE MODIFIER, SAUF POUR
# AJOUTER VOUS-MÊME D'AUTRES TESTS SI VOUS LE VOULEZ.
# NE PAS REMETTRE SUR STUDIUM. REMETTEZ SEULEMENT ponts_et_piliers.py

# THIS FILE IS ONLY USED TO CALL AND TEST YOUR CODE.
# YOU SHOULD NOT HAVE TO MODIFY IT, EXCEPT FOR ADDING
# NEW CUSTOM TESTS IF YOU WISH TO DO SO.
# DO NOT SUBMIT ON STUDIUM. ONLY SUBMIT ponts_et_piliers.py

import ponts_et_piliers as pep


def verifyAns(fileName, ExpectedVals):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    if len(lines) > len(ExpectedVals):
        raise Exception("Number of outputs greater than expected")
    elif len(lines) < len(ExpectedVals):
        raise Exception("Number of outputs lesser than expected")

    errors = []
    for i in range(len(lines)):
        if str("{0:.3f}".format(float(lines[i]))) != str(
            "{0:.3f}".format(ExpectedVals[i])
        ):
            errors.append(
                "Error on problem #"
                + str(i)
                + ", got "
                + str("{0:.3f}".format(float(lines[i])))
                + ", expected "
                + str("{0:.3f}".format(ExpectedVals[i]))
            )
    if len(errors) != 0:
        raise Exception("\n".join(errors))


if __name__ == "__main__":

    expected = [
        [3],
        [8],
        [2],
        [34],
        [49999],
        [16666647],
        [12],
        [48],
        [10],
        [8],
        [8],
        [9],
        [9],
        [10],
    ]
    for i in range(len(expected)):
        try:
            pep.main(["input" + str(i) + ".txt", "output" + str(i) + ".txt"])
            verifyAns("output" + str(i) + ".txt", expected[i])
            print("Test " + str(i) + " OK\n")
        except Exception as e:
            print("Test " + str(i) + " Fail")
            print(e)
            print()
