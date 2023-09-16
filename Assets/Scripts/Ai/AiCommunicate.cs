using UnityEngine;
using Socket;

namespace AiCharacter {
    public class AiCommunicate : MonoBehaviour
    {
        public string targetTag = "AI";  // The tag of the game objects to check proximity with
        public float proximityDistance = 2.0f;  // The distance at which the method should be triggered
        private GameObject[] objectsWithTag;
        private bool talking;

        [SerializeField] private Socket.UdpSocket socket;
        void Start() {
            // Find all game objects with the specified tag
            objectsWithTag = GameObject.FindGameObjectsWithTag(targetTag);
            talking = false;
        }

        // Update is called once per frame
        void Update()
        {
            // Loop through the found objects
            foreach (GameObject obj in objectsWithTag)
            {
                // Calculate the distance between this object and the current object in the loop
                float distance = Vector3.Distance(transform.position, obj.transform.position);

                AiCommunicate objCommunicate = obj.GetComponent<AiCommunicate>();

                // Check if the distance is less than or equal to the proximityDistance
                if (distance <= proximityDistance && obj.name != this.name && !talking && !objCommunicate.talking)
                {
                    objCommunicate.talking = true;
                    this.talking = true;
                    
                    AiCommunicate higherId = this. GetInstanceID() > obj. GetInstanceID() ? this : objCommunicate;

                    higherId.SendData(this.name + " " + obj.name);

                    while (ReceiveData() == "") {
                        this.GetComponent<RandomMovement>().enabled = false;
                        obj.GetComponent<RandomMovement>().enabled = false;
                    }

                    this.GetComponent<RandomMovement>().enabled = true;
                    obj.GetComponent<RandomMovement>().enabled = true;
                    objCommunicate.talking = false;
                    this.talking = false;
                }
            }
        }

        void SendData(string data)
        {
            socket.SendData(data);
        }

        string ReceiveData()
        {
            return socket.receivedText;
        }
    }
}