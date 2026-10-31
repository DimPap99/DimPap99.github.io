---
title: Personal Drive Mount privacy policy
description: How this personal desktop application handles Google Drive data.
eyebrow: Personal application
permalink: /personal-drive/privacy/
prose: true
---

Effective date: October 31, 2026.

This policy covers **Personal Drive Mount**, a personal rclone configuration
operated by Dimitris Papadimitriou on his own computer.

## Data access and use

The application uses Google authorization tokens to access Drive file contents
and metadata, such as filenames, folders, sizes, and modification times. It uses
this data to carry out file operations requested by the account owner.

Google API data is used only for these file-management features. It is not sold
or used for advertising, profiling, or training AI models. Use of Google API data
follows the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy),
including its Limited Use requirements.

## Storage and sharing

Rclone communicates directly between the owner's computer and Google. The
application stores authorization tokens, configuration, and cached files locally
with access restricted to the local user account. Local data remains until
removed through cache management or by the owner. Google retains cloud files
according to the owner's account settings and Google's policies.

These information pages do not receive Drive files or authorization tokens. No
Drive data is sent to the website host, rclone's developers, or other recipients
by this application.

## Revoking access and removing local data

The owner can revoke access through
[Google account permissions](https://myaccount.google.com/permissions), stop the
desktop connection, and remove its local configuration and cache. Removing local
configuration or cached copies does not delete the original Drive files.

## This website

These pages are hosted on GitHub Pages and contain no analytics, advertising,
forms, or sign-in controls. GitHub may process website request information under
its [privacy statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement).

## Contact and changes

Contact the operator using the details on the [About page]({{ '/about/' | relative_url }})
or the support email shown on Google's authorization screen. Policy changes will
be reflected in this page's effective date.

[Back to Personal Drive Mount]({{ '/personal-drive/' | relative_url }}).
