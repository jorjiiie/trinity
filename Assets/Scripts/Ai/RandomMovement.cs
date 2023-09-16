using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI; //important

public class RandomMovement : MonoBehaviour //don't forget to change the script name if you haven't
{
    NavMeshAgent agent;

    [SerializeField] LayerMask groundLayer;

    // Patrol
    Vector3 destPoint;
    bool WalkPointSet;
    [SerializeField] float WalkRange = 5.0f;

    // Anti Glitch Movement
    public float radiusThreshold = 0.1f;  // The radius within which the object is considered stationary
    public float checkInterval = 1.0f;  // How frequently to check the position (in seconds)
    public float stationaryTimeThreshold = 3.0f;  // Time threshold for considering the object as stationary

    private Vector3 lastPosition;
    private float timeStationary = 0.0f;

    void Start() {
        agent = GetComponent<NavMeshAgent>();

         // Initialize the last position to the initial position of the object
        lastPosition = this.transform.position;

        // Invoke the position check function at specified intervals
        InvokeRepeating("CheckObjectPosition", 0.0f, checkInterval);
    }

    void Update() {
        Patrol();

        // Anti Glitching
    }

    void Patrol() {
        if (!WalkPointSet) SearchForDest();
        if (WalkPointSet) agent.SetDestination(destPoint);
        if(Vector3.Distance(transform.position, destPoint) < 10) WalkPointSet = false;
    }

    void SearchForDest() {
        float z = Random.Range(-WalkRange, WalkRange);
        float x = Random.Range(-WalkRange, WalkRange);

        destPoint = new Vector3(transform.position.x + x, transform.position.y, transform.position.z + z);

        if (Physics.Raycast(destPoint, Vector3.down, groundLayer)) {
            WalkPointSet = true;
        }
    }

    private void CheckObjectPosition()
    {
        Vector3 currentPosition = this.transform.position;

        // Calculate the distance between the current and last positions
        float distance = Vector3.Distance(currentPosition, lastPosition);

        // Check if the object has moved less than the radius threshold
        if (distance <= radiusThreshold)
        {
            // Increment the time the object has been stationary
            timeStationary += checkInterval;

            // Check if the object has been stationary for the required time threshold
            if (timeStationary >= stationaryTimeThreshold)
            {
                this.transform.position += new Vector3(Random.Range(-1,1), 0, Random.Range(-1,1));
                SearchForDest();
            }
        }
        else
        {
            // Reset the time stationary if the object moved
            timeStationary = 0.0f;
        }

        // Update the last position to the current position
        lastPosition = currentPosition;
    }
}