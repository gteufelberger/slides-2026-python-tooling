def calculate_average(numbers:list[float],precision:int=2)->float:
    total=0.0
    for num in numbers:
        total+=num
    return round(total/len(numbers),precision)

def format_result(value:float,label:str="Result",show_decimal:bool=True,prefix:str=">>>",suffix:str="<<<")->str:
    if show_decimal:
        return f"{prefix} {label}: {value} {suffix}"
    return f'{prefix} {label}: {int(value)} {suffix}'
def main():
    data=[1.5,2.7,3.2,4.8,5.1]
    avg=calculate_average(data,precision=3)
    output=format_result(avg,label="Average",show_decimal=True,prefix="[",suffix="]")
    print(output)
if __name__=="__main__":
    main()
