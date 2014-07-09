#pragma strict

public var manhattan_distance: float;

public var InfoScript: Info;

function Awake(){
	InfoScript = GameObject.FindGameObjectWithTag("Info").GetComponent(Info);
}

function Start () {
	manhattan_distance = Mathf.Abs(this.transform.position.x)+Mathf.Abs(this.transform.position.y)+Mathf.Abs(this.transform.position.z);
	InfoScript.total_manhattan += manhattan_distance;
}
