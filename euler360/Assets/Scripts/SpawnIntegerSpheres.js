#pragma strict

public var sphere: Transform;
private var InfoScript: Info;
private var radius: int;

function Awake(){
	InfoScript = GameObject.FindGameObjectWithTag("Info").GetComponent(Info);
}
function Start () {
	radius = InfoScript.radius;
	PlotSpheres(radius);
	//MapCoordsToPlane(radius);	
}


function isCoordOnSphere(x,y,z,r){
	//assumes sphere is centered on the origin
	return (Mathf.Pow(x,2)+Mathf.Pow(y,2)+Mathf.Pow(z,2) == Mathf.Pow(r,2));
}

function PlotSpheres(radius:int){
	for (var x = -radius; x<radius+1; x++){
		for (var y = -radius; y<radius+1; y++){
			for (var z = -radius; z<radius+1; z++){
				if ( isCoordOnSphere(x,y,z,radius) )
					var go = Instantiate(sphere,Vector3(x,y,z),Quaternion.identity);
			}		
		}
	}
}

function MapCoordsToPlane(radius:int){
	for (var x = -radius; x<radius+1; x++){
		for (var y = -radius; y<radius+1; y++){
			for (var z = 0; z<radius+1; z++){
				//if ( (x==0||y==0||z==0) && isCoordOnSphere(x,y,z,radius) ){
				//if ( (x!=0&&y!=0&&z!=0) && isCoordOnSphere(x,y,z,radius) ){
				if ( isCoordOnSphere(x,y,z,radius) ){
					var colorChange = false;
					var a: float;
					var b: float;
					if(z!=0){
						a = x/z;
						b = y/z;
						if(a==0 || b==0)
							colorChange = true;
						
					}else{
						a = x/.5f;
						b = y/.5f;
						colorChange = true;	
					}
					var go = Instantiate(sphere,Vector3(a,b,0),Quaternion.identity);
					if(colorChange)
						go.renderer.material.color = Color.red;
				}
			}		
		}
	}
}