def interactor_verdict():
    print("Please, input task code:\n")
    task_code = int(input())
    print("Please, input interactor result:\n")
    interactor_result = int(input())
    print("Please, input checker result:\n")
    checker_result = int(input())

    if (127 < task_code) | (-127 > task_code):
        print("TaskCode Error")
        pass
    if (7 < interactor_result) | (0 > interactor_result):
        print("InteractorResult Error")
        pass
    if (7 < checker_result) | (0 > checker_result):
        print("CheckerResult Error")
        pass

    if interactor_result == 0:
        if task_code != 0:
            return 3
        else:
            return checker_result

    elif interactor_result == 1:
        return checker_result

    elif interactor_result == 4:
        if task_code != 0:
            return 3
        else:
            return 4

    elif interactor_result == 6:
        return 0

    elif interactor_result == 7:
        return 1

    else:
        return interactor_result


verdict = interactor_verdict()
print(verdict)
