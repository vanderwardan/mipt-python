import argparse
import sys


def format(input_name, output_name, w, b):
    if (input_name == sys.stdin):
        input = sys.stdin
    else:
        input = open(input_name, "r")
    if (output_name == sys.stdout):
        output = sys.stdout
    else:
        output = open(output_name, "w")

    text = input.read()

    words = getWords(text)

    if (not checkPossible(words, b, w)):
        print("Process fnished with exit code 1")
        raise SystemExit(1)

    line_size = 0
    isParagraph = True

    for ind in range(0, len(words)):
        if (words[ind] == '\n'):
            if (ind > 0 and words[ind - 1] == '\n'):
                output.write('\n')
                line_size = 0
                isParagraph = True
        elif (not checkASCII(words[ind][0])):
            if (isParagraph):
                printIndent(b, output)
                line_size = b
                # we'll change isParagraph later

            # calc how many letters we need for this word + marks
            tmpLen = len(words[ind])
            tmpInd = ind + 1
            while (tmpInd < len(words) and checkASCII(words[tmpInd][0])):
                tmpLen += len(words[tmpInd])
                tmpInd += 1

            assert (tmpLen <= w)

            if (line_size != 0 and not isParagraph):  # for space before word
                tmpLen += 1
            if (line_size + tmpLen <= w):
                if (line_size != 0 and not isParagraph):
                    output.write(' ')
                    line_size += 1
                output.write(words[ind])
                line_size += len(words[ind])
            else:
                assert (not isParagraph)

                output.write('\n' + words[ind])
                line_size = len(words[ind])

            # as I promised
            if (isParagraph):
                isParagraph = False
        else:
            if (isParagraph):
                printIndent(b, output)
                line_size = b
                isParagraph = False
            output.write(words[ind])
            line_size += len(words[ind])


# return sequence(words, marks, \n), skipping spaces, or ' ' if the aren't
def getWords(str):
    pos = 0
    words = []
    while (pos < len(str)):
        while (str[pos] == ' ' and pos < len(str) - 1):
            pos += 1
        oldpos = pos

        if (checkASCII(str[pos])):
            words.append(str[pos])
            pos += 1
        else:
            while (pos < len(str) and str[pos] != ' ' and str[pos] != '\n'
                   and not checkASCII(str[pos])):
                pos += 1
            if (pos == len(str)):
                words.append(str[oldpos:pos])
            elif (str[pos] == '\n'):
                if (pos > oldpos):
                    words.append(str[oldpos:pos])
                words.append('\n')
                pos += 1
            else:
                words.append(str[oldpos:pos])
    return words


# print indent containing p spaces
def printIndent(x, out):
    for i in range(0, x):
        out.write(' ')


def checkASCII(c):
    a = ord(c)
    if (a == 44 or a == 46 or a == 63 or a == 33 or a == 45
        or a == 58 or a == 39):
        return True
    return False


def checkPossible(words, b, w):
    line_size = 0
    isParagraph = True

    for ind in range(0, len(words)):
        if (words[ind] == '\n'):
            if (line_size != 0):
                line_size = 0
            else:
                isParagraph = True
        elif (not checkASCII(words[ind][0])):
            if (isParagraph):
                line_size = b
                # we'll change isParagraph later

            # calc how many letters we need for this word + marks
            tmpLen = len(words[ind])
            tmpInd = ind + 1
            while (tmpInd < len(words) and checkASCII(words[tmpInd][0])):
                tmpLen += len(words[tmpInd])
                tmpInd += 1

            if (tmpLen > w):
                return False
            if (line_size != 0 and not isParagraph):  # for space before word
                tmpLen += 1
            if (line_size + tmpLen <= w):
                if (line_size != 0 and not isParagraph):
                    line_size += 1
                line_size += len(words[ind])
            else:
                if (isParagraph):
                    return False
                line_size = len(words[ind])

            # as I promised
            if (isParagraph):
                isParagraph = False
        else:
            if (isParagraph):
                line_size = b
                isParagraph = False
            line_size += len(words[ind])
    return True


def main():
    parser = argparse.ArgumentParser(description="Format text")
    parser.add_argument('-i', '--input', type=str, default=sys.stdin,
                        help='input file name')
    parser.add_argument('-o', '--output', type=str, default=sys.stdout,
                        help='output file name')
    parser.add_argument('-l', '--line-length', type=int, default=None,
                        help='max line length')
    parser.add_argument('-p', '--paragraph-spaces', type=int, default=None,
                        help='amount of spaces for paragraph')
    args = parser.parse_args()
    format(args.input, args.output, args.line_length, args.paragraph_spaces)


if __name__ == '__main__':
    main()
