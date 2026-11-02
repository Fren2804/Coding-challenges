
def getKnowledgeDisparity(expertise):
    expertise.sort()
    expertise.reverse()
    values = []
    if len(expertise) < 3:
        return (0)
    for i in range(len(expertise) - 1):
        values.append(expertise[i] - expertise[i + 1])
    first = True
    minimun_value = 0
    for i in range(len(values) - 1):
        if first:
            minimun_value = values[i] + values[i + 1]
            first = False
        else:
            suma = values[i] + values[i + 1]
            if suma < minimun_value:
                minimun_value = suma
    return (minimun_value)


def main():
    expertise = [10, 7, 14, 5, 18, 1]
    print(getKnowledgeDisparity(expertise))
    


if __name__ == "__main__":
    main()
