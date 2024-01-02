# AWS Cloud Cost Optimization - Identifying Stale Resource


## Identifying  Stale EBS Snapshots -

 In this example, we'll carate the Lambda function that identifies EBS snapshots that are no longer associated with amy active EC2 instances and delete them to save on storage cost.

#### DESCRIPTION 

The Lambda function fetches EBS snapshots owned by the same account and also retrives a list of the ec2 instances. For each snapshot, it checks if the associated volume is not associated with any active instance if it finds a stale snapshot it deletes it effectively optomizing storage cost.
