# TODO: confirm that this is correct + write tests

"""def tryAdd(xParts, toDo, mostLeastData, currentFill, noBegin, MIN, MAX, usedPart):
chooseFrom = [MIN, MAX]

if mostLeastData["whichMost"] == 1:
    toAddMaxMin = [-add + 3 for add in toDo["add"]]
else:
    toAddMaxMin = toDo["add"]

toAdd = chooseFrom[toAddMaxMin[0] - 1]

done = 0  # Flag to check if something is added

# Check if there are enough resources
if currentFill["toUse"][0] >= sum(
    [1 for val in toAddMaxMin if val == 1]
) and currentFill["toUse"][1] >= sum([1 for val in toAddMaxMin if val == 2]):
    # Iterate through all parts
    for i in range(len(currentFill["toFill"])):
        # Check if there is enough space in specific part
        if currentFill["toFill"][i] >= len(toAdd):
            if toDo["doAdd"]:  # We need to add to part
                if usedPart[i] > 0:
                    if toDo[
                        "makeDiff"
                    ]:  # Extra part must make MINMAX jump with existing part
                        if xParts[i][-1] != toAdd[0]:
                            xParts[i].append(toAdd)
                            done = 1
                            currentFill = updateUseFill(
                                toAddMaxMin,
                                currentFill["toUse"],
                                currentFill["toFill"],
                                i,
                            )
                            break
                        elif xParts[i][0] != toAdd[0] and not noBegin[i]:
                            xParts[i] = [toAdd[::-1]] + xParts[i]
                            done = 1
                            currentFill = updateUseFill(
                                toAddMaxMin,
                                currentFill["toUse"],
                                currentFill["toFill"],
                                i,
                            )
                            break
                    else:  # Extra part must not make a MINMAX jump with existing part
                        xParts[i].append(toAdd)
                        done = 1
                        currentFill = updateUseFill(
                            toAddMaxMin,
                            currentFill["toUse"],
                            currentFill["toFill"],
                            i,
                        )
                        break
            else:  # We need to start a new part
                if usedPart[i] == 0:
                    usedPart[i] = 1
                    xParts[i] = [toAdd]
                    done = 1
                    currentFill = updateUseFill(
                        toAddMaxMin, currentFill["toUse"], currentFill["toFill"], i
                    )
                    break

if done == 1:
    nextPhase = toDo["goToOk"]
else:
    nextPhase = toDo["goToNotOk"]

output = {
    "xParts": xParts,
    "currentFill": currentFill,
    "nextPhase": nextPhase,
    "usedPart": usedPart,
}

return output
"""
