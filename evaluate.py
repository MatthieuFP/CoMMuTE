import sys

def read_file(fpath: str):
    with open(fpath, "r") as f:
        return f.read().strip("\n").split("\n")

def float_conversion(scores: list):
    return [float(s) for s in scores]

if __name__ == "__main__":
    correct = float_conversion(read_file(sys.argv[1]))
    incorrect = float_conversion(read_file(sys.argv[2]))
    preds = [int(c < i) for c, i in zip(correct, incorrect)]
    accuracy = sum(preds) / len(preds)
    print("Score on CoMMuTE : {:4f}".format(accuracy))
