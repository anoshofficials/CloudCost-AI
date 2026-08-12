# Day 6 – IAM Roles and Permissions

## Objective

Understand how predefined IAM roles work in Google Cloud and how roles provide a collection of permissions.

## What I Learned

IAM roles are collections of permissions that determine what actions a principal can perform on Google Cloud resources.

Today I explored three predefined IAM roles:

- `roles/viewer`
- `roles/editor`
- `roles/owner`

## IAM Role Model

```text
Principal
    ↓
Role
    ↓
Permissions

A principal is assigned a role, and the role provides a defined set of permissions.

Hands-on: Inspecting IAM Roles

I used the Google Cloud CLI to inspect the predefined IAM roles.

Owner
gcloud iam roles describe roles/owner
Editor
gcloud iam roles describe roles/editor
Viewer
gcloud iam roles describe roles/viewer
Permission Comparison

I used the following command to examine the permission entries included in each role:

gcloud iam roles describe roles/editor \
  --format="value(includedPermissions)" | tr ';' '\n' | wc -l

The same approach was used to inspect the Viewer and Owner roles.

The results from my current Google Cloud environment were:

IAM Role	Reported Permission Entries
Viewer	6,030
Editor	11,911
Owner	13,497

These results helped me understand that predefined IAM roles provide different levels and scopes of access.

Key Learning

The main lesson from today's exercise was:

A role is not just a name. A role contains a collection of permissions.

The broader the role, the more access it can provide.

This connects directly with the Principle of Least Privilege.

In a production environment, users and services should receive only the permissions they actually need instead of unnecessarily broad access.

What I Practiced
Inspected predefined IAM roles
Compared Viewer, Editor, and Owner roles
Examined includedPermissions
Used the gcloud CLI for IAM role inspection
Compared permission sets
Connected IAM roles with the Principle of Least Privilege
Day 6 Progress
Completed
IAM role inspection
Viewer role
Editor role
Owner role
Permission comparison
Least Privilege understanding
Next
Service Accounts
Service Account roles
Workload authentication
Least Privilege for applications
IAM security best practices

Another hands-on step completed in the CloudCost AI journey.
