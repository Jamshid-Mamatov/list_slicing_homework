def main(list1):
    """
    A list of several elements is given. Reverse this list.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    l=len(list1)
    for i in range(l//2):
        value=list1[i]
        list1[i]=list1[l-1-i]
        list1[l-1-i]=value

    return list1[::-1]
