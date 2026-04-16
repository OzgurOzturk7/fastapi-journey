# OBSERVATIONS.md

## 1. Image Size

The postgres:16-alpine image is around 110MB on disk. I would call it medium-small. It is not a tiny image because PostgreSQL is not a simple tool — it includes the full database server, helper utilities, libraries, and runtime dependencies. The alpine base helps keep it smaller than it would be on a standard Linux distro, but the PostgreSQL binaries themselves add significant size.

## 2. Image Layers

The image has around 24 layers in total. Most layers are small configuration steps like setting environment variables or creating directories. The largest layer by far is the one that runs the PostgreSQL installation — it downloads and compiles the PostgreSQL binaries along with all their dependencies, which accounts for around 273MB of the build.

## 3. OS and Architecture

From `docker inspect`, the image uses:
- **Os:** linux
- **Architecture:** amd64

## 4. Postgres-specific: Why did the data disappear?

When I ran `docker rm`, I was not just stopping a process — I was deleting the entire writable layer that belonged to that container. All data written during the container's lifetime lives in that writable layer, so when the container is removed, the data goes with it. To make data persist across container restarts and removals, a volume must be mounted to `/var/lib/postgresql/data`. Without a volume, every new container starts completely fresh.

## 5. What surprised me most

What surprised me most was how the data disappeared completely after removing and recreating the container. At first glance it feels like: database is running, data is being saved, so it must be permanent. But in Docker the reality is different — a container is a temporary runtime, and data is only permanent if a volume is attached. Seeing the `relation does not exist` error after recreating the container made this concept click immediately.
