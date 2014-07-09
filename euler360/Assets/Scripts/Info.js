#pragma strict

public var total_manhattan: int;
public var total_raised_fifth: int;
@Range(1,90)
public var radius: int;



function Update(){
	total_raised_fifth = Mathf.Pow(total_manhattan,5);
}	