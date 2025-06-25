from torch.distributed.device_mesh import init_device_mesh

mesh_2d = init_device_mesh("cuda", (2, 4), mesh_dim_names=("replicate", "shard"))

# Users can access the underlying process group thru `get_group` API.
replicate_group = mesh_2d.get_group(mesh_dim="replicate")
shard_group = mesh_2d.get_group(mesh_dim="shard")
print(f"{replicate_group = } {replicate_group.size() = } {replicate_group.rank() = }")
print(f"{shard_group = } {shard_group.size() = } {shard_group.rank() = }")
shard_mesh = mesh_2d["shard"]
dp_rank = shard_mesh.get_local_rank()
print(f"{dp_rank = }")