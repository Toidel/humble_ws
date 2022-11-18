from dataclasses import dataclass
import json
from typing import List, Optional, Dict
from model.operation import Operation, Transition
from predicates.state import State
import predicates.guards
import predicates.actions
from predicates.guards import AlwaysTrue, Guard, And
from predicates.guards import AlwaysFalse

@dataclass
class Model(object):
    initial_state: State
    operations: Dict[str, Operation]
    transitions: List[Transition]

    def __post_init__(self):
        ops = {o: "i" for o in self.operations}
        self.initial_state = self.initial_state.next(**ops)

g = predicates.guards.from_str
a = predicates.actions.from_str


def the_model() -> Model:

    initial_state = State(
        # control variables
        robot_run = False,   # trigger action when true. Change to false and then to true to trigger again
        robot_command = 'move_j',
        robot_velocity = 2.0,
        robot_acceleration = 0.5,
        robot_goal_frame = 'unknown',   # where to go with the tool tcp
        robot_tcp_frame = 'r1_svt_tcp', # the tool tcp to use
        gripper_run = False, # trigger service when true. Change to false and then to true to trigger again
        gripper_command = 'none', # pick_red, pick_green, pick_blue, drop_red, drop_green, drop_blue
        robot_pose = "unknown",
        goal_as_string = "",
        replan = False,

        # measured variables
        robot_state = "initial",  # "exec", "done", "failed" 
        replanned = False,

        #estimated
        green_cube_at = "pose_1", # pose_1, pose_2, pose_3, gripper, buffer
        red_cube_at = "pose_2",  # pose_1, pose_2, pose_3, gripper, buffer
        blue_cube_at = "pose_3",  # pose_1, pose_2, pose_3, gripper, buffer
    )

    # we will store all operations in this dict that will be part of the model
    ops = {}

    # this is maybe the simplest operation, to make the rrobot robot to the buffer position
    ops[f"op_move_to_buffer"] = Operation(

        
        name = f"op_move_to_buffer",

        
        precondition = Transition("pre", 
            g(f"!robot_run && robot_state == initial && robot_pose != buffer"), 
            a(f"robot_command = move_j, robot_run, robot_goal_frame = buffer")),

        
        postcondition = Transition("post", 
            g(f"robot_state == done"), 
            a(f"!robot_run, robot_pose <- buffer")),
        
        
        effects = (),
        to_run = Transition.default()
    )

    for i in [1,2,3]:
        ops[f"op_move_to_pose_{i}"] = Operation(

        
        name = f"op_move_to_pose_{i}",

        
        precondition = Transition("pre", 
            g(f"!robot_run && robot_state == initial && robot_pose != pose_{i}"), 
            a(f"robot_command = move_j, robot_run, robot_goal_frame = pose_{i}")),

        
        postcondition = Transition("post", 
            g(f"robot_state == done"), 
            a(f"!robot_run, robot_pose <- pose_{i}")),
        
        
        effects = (),
        to_run = Transition.default()
    )
    ops[f"op_pick_green_cube"] = Operation(
        name = f"op_pick_green_cube",
        precondition = Transition("pre", 
            g(f"(robot_pose == green_cube_at) && !gripper_run && green_cube_at"), 
            a(f"robot_command = pick, robot_tcp_frame = r1_svt_tcp, robot_run")),
        postcondition = Transition("post", 
            g(f"robot_state == done"), 
            a(f"!robot_run, gripper_run, !green_cube_at_pose_1")),
        effects = (),
        to_run = Transition.default()
    )
    ops[f"drop_pose_1"] = Operation(
        name = f"drop_pose_1",
        precondition = Transition("pre", 
            g(f"!robot_run && robot_state == initial && (robot_pose == pose_1) && gripper_run && !cube_at_pose_1"), 
            a(f"robot_command = drop, robot_tcp_frame = r1_svt_tcp, robot_run")),
        postcondition = Transition("post", 
            g(f"robot_state == done"), 
            a(f"!robot_run, gripper_run, cube_at_pose_1")),
        effects = (),
        to_run = Transition.default()
    )

    
    
    # here is another example of two dummy operations showing that you can use an iterator to 
    # create multiple operations at the same time
    # for i in [1,2]:
    #     ops[f"op{i}"] = Operation(
    #         name=f"op{i}", 
    #         precondition=Transition("pre", g(f"(!v{i}) && (dummy == hello)"), a(f"v{i}")),
    #         postcondition=Transition("post", AlwaysTrue(), a(f"dummy <- world")),
    #         effects=(),
    #         to_run = Transition.default()
    #     )

    # Now you can add all the other operations that you need to make the robot to move between the positions
    # and to pick and place the cubes.

    # add the rest of the operations here: 
    # ops[f"op_pick_red_cube"] = Operation(...

    # To be used to run "free" transitions. 
    # Example: setting a new goal in a specific state
    transitions: List[Transition] = []

    return Model(
        initial_state,
        ops,
        transitions
    )

def from_goal_to_goal(state: State) -> Guard:
    """
    Create a goal predicate 
    """
    goal: str = state.get("goal_as_string")
    if goal != "":
        return g(goal)
    
    return AlwaysFalse()