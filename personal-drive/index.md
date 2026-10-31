---
title: Personal Drive Mount
description: A personal desktop connection to Google Drive, using rclone.
eyebrow: Personal application
permalink: /personal-drive/
prose: true
---

Personal Drive Mount is maintained by Dimitris Papadimitriou for use on his own
computer. It connects his Google Drive account to the desktop file manager
through [rclone](https://rclone.org/).

## What the application does

After the account owner authorizes access, rclone can list, download, upload,
rename, edit, and delete Drive files and folders in response to desktop file
operations or commands. The connection loads files as needed and uses a local
cache to support file access.

Authorization is handled by Google. Account access is limited to the permissions
the owner grants to this application.

## Privacy and contact

Read the [Personal Drive Mount privacy policy]({{ '/personal-drive/privacy/' | relative_url }})
for details about data access, local storage, and revoking authorization.

For questions, use the contact details on the
[owner's About page]({{ '/about/' | relative_url }}) or the support email shown on
the Google authorization screen.
