def longestcommonprefix(str: list[str]) -> str:
    prefix = str[0]
    # Use len(prefix) instead of just prefix
    for i in range(len(prefix)):
        for word in str:
            if i == len(word) or prefix[i] != word[i]:
                return prefix[:i]
    return prefix

print(longestcommonprefix(["flowers", "flow", "fly", "flight"]))
