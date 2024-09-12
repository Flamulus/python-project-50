
def diff(items1, items2):

    def walk(items1, items2, depth):
        keys = sorted(set(items1.keys()) | set(items2.keys()))
        result = {}
        for key in keys:
            if (key in items1) and (key in items2):
                
                if items1[key] == items2[key]:
                    result[key] = {"value": items1[key], "diff": "", "depth": depth}
                
                else:
                    
                    if isinstance(items1[key], dict) and isinstance(items2[key], dict):
                        result[key] = {
                            "value": walk(items1[key], items2[key], depth + 1),
                            "diff": "-",
                            "depth": depth
                        }
                    else:
                        result[key] = [
                            {"value": items1[key], "diff": "-", "depth": depth}, 
                            {"value": items2[key], "diff": "+", "depth": depth}
                        ]

            elif (key in items1):
                result[key] = {"value": items1[key], "diff": "-", "depth": depth}

            elif (key in items2):
                result[key] = {"value": items2[key], "diff": "+", "depth": depth}
        return result
    
    return walk(items1, items2, 0)


if __name__ == "__main__":
    from gendiff.parser import parse_files

    file1, file2 = parse_files(
        "/home/flamulus/education/python-project-50/tests/fixtures/file1.json",
        "/home/flamulus/education/python-project-50/tests/fixtures/file2.json"
    )

    d_r = diff(file1, file2)
    print(d_r)

