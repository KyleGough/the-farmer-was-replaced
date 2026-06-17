# Distributes 32 drones across a column of tiles as fast as possible using a binary split.
# fn is a function that will be called when the drone is ready.
# `move()` calls are unpacked from for loops to save ticks.

def distribute_drones(fn):
	spawn_drone(top_half_distribute, fn)
	bottom_half_distribute(fn)

def top_half_distribute(fn):
	move(South)
	spawn_drone(partition_8, South, fn)
	spawn_drone(partition_4, South, fn)
	spawn_drone(partition_2, South, fn)
	spawn_drone(partition_1, South, fn)
	fn()

def bottom_half_distribute(fn):
	spawn_drone(partition_8, North, fn)
	spawn_drone(partition_4, North, fn)
	spawn_drone(partition_2, North, fn)
	spawn_drone(partition_1, North, fn)
	fn()

def partition_8(direction, fn):
	move(direction)
	move(direction)
	move(direction)
	move(direction)
	move(direction)
	move(direction)
	move(direction)
	move(direction)
	spawn_drone(partition_4, direction, fn)
	spawn_drone(partition_2, direction, fn)
	spawn_drone(partition_1, direction, fn)
	fn()

def partition_4(direction, fn):
	move(direction)
	move(direction)
	move(direction)
	move(direction)
	spawn_drone(partition_2, direction, fn)
	spawn_drone(partition_1, direction, fn)
	fn()

def partition_2(direction, fn):
	move(direction)
	move(direction)
	spawn_drone(partition_1, direction, fn)
	fn()

def partition_1(direction, fn):
	move(direction)
	fn()
