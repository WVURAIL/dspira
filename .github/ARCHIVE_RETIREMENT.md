# Retired repositories

The active DSPIRA release `preserved-repositories-2026-09-25` owns the recovery
packages for dspira-archive, cra, gr-dspira, gr-transient, and dspira-lessons.
The retired repositories' default branches contain forwarding notices only.
Their Git history is intentionally retained until a separate deletion decision.

## Software repository name swap

On September 25, the original `gr-dspira` repository became the active
`dspira-software` repository. Its GitHub repository ID is `139190089`.
Its default branch includes the current software and both projects' Git histories.
Its original star, fork, and contributor history remain attached to that repository.

The former `dspira-software` repository now uses the name `gr-dspira`.
Its GitHub repository ID is `1386771762`. It is archived and contains only the
forwarding notice on its default branch. Both software issues moved to the
active repository and retained their numbers.

The `gr-dspira-preserved.zip` package remains an unchanged historical snapshot
from before this swap. Verify repository IDs before any future deletion.
Do not delete the active `dspira-software` repository.

## What was preserved

`_data/preserved_repositories.json` records the original commits and checksums.
The five ZIPs contain 573 default-branch files, complete advertised Git refs,
branches and tags, public GitHub records, and restoration instructions.
The institute archive also contains its wiki and all 35 historical LFS objects.
Its 21 pull requests are exported as JSON, including reviews and event records.
The other repositories have no issue or pull-request records and no wiki content.
No repository has Discussions enabled. Existing release metadata is included;
the one old release has no attached assets beyond its Git tag.

Every bundle was cloned into a fresh mirror and checked with `git fsck --full`.
Restored refs match the source mirrors. Default-branch files were extracted from
restored Git objects. Every source file and LFS object has a SHA256 verification.
The ZIP files were also read back and checked. Historical file modes and symlinks
are retained in Git, even where the convenience source folder uses plain files.

## Website ownership

- DSPIRA publishes historical content under `/dspira/history/sites/`.
- The lab repository publishes HTML redirects at `/dspira-archive/`, `/cra/`,
  `/gr-transient/`, `/gr-dspira/`, and `/dspira-lessons/`.
- Existing non-HTML download URLs retain byte-identical copies. GitHub Pages
  cannot send configurable HTTP redirects for individual static download files.
- Historical HTML redirects preserve query strings and fragments.
- The lab workflow runs hourly to refresh current lesson redirects.
- DSPIRA and the lab site load the pinned `retired-sites.zip` release asset.
  They never check out a retired repository.
- `_data/retired_sites.json` pins the release URL and SHA256. Extraction validates
  the checksum and rejects unsafe archive paths before writing files.

The retired-sites asset includes deployed institute and CRA artifacts. The
transient site was rebuilt from its exact preserved commit because its old
deployment artifact had expired. The source package retains its original files.
The active site adds historical labels, current canonical URLs, and noindex.
These presentation changes do not modify the source recovery packages.

## Restoring a repository

Download its ZIP and `SHA256SUMS` from the release. Verify the download, then
extract it. Inside the extracted repository folder:

```sh
git clone --mirror REPOSITORY.bundle REPOSITORY.git
# If lfs/ exists, copy it into REPOSITORY.git/lfs/ before restoring LFS hosting.
git -C REPOSITORY.git fsck --full
git -C REPOSITORY.git remote set-url origin NEW_REPOSITORY_URL
git -C REPOSITORY.git push --mirror
git -C REPOSITORY.git lfs push --all origin
```

Restore a wiki from its separate bundle. The `github/` folder contains public
discussion and release records. Importing those records requires separate work;
pushing Git alone does not recreate issues, pull requests, or release pages.

## Before any future deletion

Keep a downloaded copy of the recovery release outside GitHub. Recheck release
asset hashes and the latest DSPIRA and lab deployments. Verify old
HTML addresses and representative PDF/data downloads after disabling each
retired repository's Pages deployment. Search active workflow files for old
repository checkouts. Check for any new refs or changes since the snapshot.

Deleting a repository permanently removes its original GitHub repository,
raw-file, commit, issue, pull-request, release, and wiki URLs. Stars, watcher
subscriptions, permissions, and repository relationships are not restored by
these packages. Existing external clones and forks are outside our control.
The forwarding README also disappears after deletion. The lab-owned website
redirects and active DSPIRA recovery packages continue to work independently.

Repository deletion is a separate, explicit decision. This migration prepares
the content and websites; it does not delete the repositories.
