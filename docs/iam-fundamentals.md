# Day 5 – IAM Fundamentals

## Objective

Understand the basics of Identity and Access Management (IAM) in Google Cloud and inspect the IAM policy of the CloudCost AI project.

## What I Learned

- IAM controls access to Google Cloud resources.
- A Principal identifies who or what is requesting access.
- A Role is a collection of permissions.
- Permissions define which actions can be performed.
- IAM policies connect principals with roles.
- Project-level IAM policies control access to resources within the project.

## IAM Model

Principal → Role → Permissions

Example:

User
→ roles/owner
→ CloudCost AI Project

## IAM Policy Inspection

Command used:

```bash
gcloud projects get-iam-policy cloudcost-ai
