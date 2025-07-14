# FSM csv to Verilog

    # Verilog Schema
import copy
from enum import IntEnum

tab_len = 4

keyword_verilog = [
# 소괄호, 대괄호, 세미콜론, 공백, 
# B/E, 모듈 B/E, 
# Continuous/Procedural Assignment, 
# if, elif, else, case(x,z) B/E
    "(", ")",
    "[", "]",
    ";", ":", " ",
    "begin", "end",
    "module", "endmodule",
    "assign", "always",
    "if", "else"
    "case", "casex", "casez",
    "endcase",
    "wire", "reg",
    "parameter", "localparam",
    "=", "input", "output"
]

class tokenList_verilog(IntEnum):
    BRACKET_B = 0
    BRACKET_E = 1
    B_BRACKET_B = 2
    B_BRACKET_E = 3
    SEMICOLON = 4
    COLON = 5
    SPACE = 6
    BEGIN = 7
    END = 8
    MODULE_B = 9
    MODULE_E = 10
    ASSIGN = 11
    ALWAYS = 12
    IF = 13
    ELSE = 14
    CASE = 15
    CASEX = 16
    CASEZ = 17
    CASE_E = 18
    WIRE = 19
    REG = 20
    PARAMETER = 21
    LOCALPARAM = 22
    EQUAL = 23
    INPUT = 24
    OUTPUT = 25

keyword_name = ""
keyword_field = ""
keyword_content = ""
keyword_len = 0

verilogSchema_module = [
    [
        keyword_verilog[tokenList_verilog.MODULE_B], 
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_name,
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E], 
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.MODULE_E] ]
]

verilogSchemaComponent_wireType = [
    [
        keyword_verilog[tokenList_verilog.WIRE], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_regType = [
    [
        keyword_verilog[tokenList_verilog.REG], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_wireLenType = [
    [
        keyword_verilog[tokenList_verilog.WIRE], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],  
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_regLenType = [
    [
        keyword_verilog[tokenList_verilog.REG], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],   
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_parameterType = [
    [
        keyword_verilog[tokenList_verilog.PARAMETER], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_localparamType = [
    [
        keyword_verilog[tokenList_verilog.LOCALPARAM], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_parameterLenType = [
    [
        keyword_verilog[tokenList_verilog.PARAMETER], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],  
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_localparamLenType = [
    [
        keyword_verilog[tokenList_verilog.LOCALPARAM], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],   
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_inputType = [
    [
        keyword_verilog[tokenList_verilog.INPUT], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_outputType = [
    [
        keyword_verilog[tokenList_verilog.OUTPUT], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_outputregType = [
    [
        keyword_verilog[tokenList_verilog.OUTPUT], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.REG], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_inputLenType = [
    [
        keyword_verilog[tokenList_verilog.INPUT], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],  
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_outputLenType = [
    [
        keyword_verilog[tokenList_verilog.OUTPUT], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],   
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchemaComponent_outputregLenType = [
    [
        keyword_verilog[tokenList_verilog.OUTPUT], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.REG], 
        keyword_verilog[tokenList_verilog.SPACE], 
        keyword_verilog[tokenList_verilog.B_BRACKET_B], 
        str(keyword_len-1), ":0",
        keyword_verilog[tokenList_verilog.B_BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],   
        keyword_verilog[tokenList_verilog.EQUAL],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchema_assign = [
    [
        keyword_verilog[tokenList_verilog.ASSIGN],
        keyword_content,
        keyword_verilog[tokenList_verilog.SEMICOLON]
    ]
]

verilogSchema_always = [
    [
        keyword_verilog[tokenList_verilog.ALWAYS], 
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_field,
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BEGIN]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.END] ]
]

verilogSchemaComponent_if = [
    [
        keyword_verilog[tokenList_verilog.IF], 
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BEGIN]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.END] ]
]

verilogSchemaComponent_elseif = [
    [
        keyword_verilog[tokenList_verilog.ELSE], 
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.IF], 
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BEGIN]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.END] ]
]

verilogSchemaComponent_else = [
    [
        keyword_verilog[tokenList_verilog.ELSE], 
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E],
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BEGIN]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.END] ]
]

verilogSchema_case = [
    [ 
        keyword_verilog[tokenList_verilog.CASE], 
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.CASE_E] ]
]

verilogSchema_casex = [
    [ 
        keyword_verilog[tokenList_verilog.CASEX], 
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.CASE_E] ]
]

verilogSchema_casez = [
    [ 
        keyword_verilog[tokenList_verilog.CASEZ], 
        keyword_verilog[tokenList_verilog.BRACKET_B], 
        keyword_field,
        keyword_verilog[tokenList_verilog.BRACKET_E]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.CASE_E] ]
]

verilogSchemaComponent_caseElement = [
    [ 
        keyword_field,
        keyword_verilog[tokenList_verilog.COLON],
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BEGIN]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.END] ]
]

verilogSchemaComponent_defaultElement = [
    [ 
        "default",
        keyword_verilog[tokenList_verilog.COLON],
        keyword_verilog[tokenList_verilog.SPACE],
        keyword_verilog[tokenList_verilog.BEGIN]
    ],
    [ keyword_content ],
    [ keyword_verilog[tokenList_verilog.END] ]
]

def caseBuild(target, conditions, contents, type):
    # type 0: case, type 1: casex, type 2: casez
    # condition-contents pair로 (conditions는 n-1개, contents는 n개)
    # case[x,z](_target)
    #   _conditions[0]: begin
    #       _contents[0]
    #   end
    #   ...
    #   _conditions[n-1]: begin
    #       _contents[0]
    #   end
    #   default: begin
    #       _contents[n]
    #   end
    # endcase
    # 를 생성하는 함수

    elements = []

    for idx in range(0, len(conditions)):
        keyword_field = conditions[idx]
        keyword_content = contents[idx]
        element = copy.deepcopy(verilogSchemaComponent_caseElement)
        elements.append(element)

    keyword_content = contents[-1]
    element = copy.deepcopy(verilogSchemaComponent_defaultElement)
    elements.append(elements)

    keyword_field = target
    keyword_content = elements

    if (type == 0):
        resultBuild = copy.deepcopy(verilogSchema_case)
    elif (type == 1):
        resultBuild = copy.deepcopy(verilogSchema_casex)
    elif (type == 2):
        resultBuild = copy.deepcopy(verilogSchema_casez)

    return resultBuild

def ifelseBuild(conditions, contents):
    # condition-contents pair로 (conditions는 n-1개, contents는 n개)
    # if (_conditions[0]) begin
    #   _contents[0]
    # end
    # ...
    # else if (_conditions[n-1]) begin
    #   _contents[n-1]
    # end
    # else begin
    #   _contents[n]
    # end
    # 를 생성하는 함수
    
    elements = []

    keyword_field = conditions[0]
    keyword_content = contents[0]
    element = copy.deepcopy(verilogSchemaComponent_if)
    elements.append(element)

    for idx in range(1, len(conditions)):
        keyword_field = conditions[idx]
        keyword_content = contents[idx]
        element = copy.deepcopy(verilogSchemaComponent_elseif)
        elements.append(element)

    keyword_content = contents[-1]
    element = copy.deepcopy(verilogSchemaComponent_else)
    elements.append(elements)

    return elements

def assignBuild(content):
    # content는 1개
    # assign _content;
    # 를 생성하는 함수

    keyword_content = content

    resultBuild = copy.deepcopy(verilogSchema_assign)

    return resultBuild

def alwaysBuild(condition, content):
    # condition, content는 1개
    # always _condition begin
    #   _content
    # end
    # 를 생성하는 함수

    keyword_field = condition
    keyword_content = content

    resultBuild = copy.deepcopy(verilogSchema_always)

    return resultBuild

def dataTypeBuild(type, name, len):
    # name, len는 1개
    # wire/reg/parameter/localparam name; len <= 1
    # wire/reg/parameter/localparam [len-1:0] name; len > 1
    # 를 생성하는 함수

    keyword_content = name
    keyword_len = len

    if (len <= 1): 
        if (type == 0):
            resultBuild = copy.deepcopy(verilogSchemaComponent_wireType)
        elif (type == 1):
            resultBuild = copy.deepcopy(verilogSchemaComponent_regType)
        elif (type == 2):
            resultBuild = copy.deepcopy(verilogSchemaComponent_parameterType)
        elif (type == 3):
            resultBuild = copy.deepcopy(verilogSchemaComponent_localparamType)
    else:
        if (type == 0):
            resultBuild = copy.deepcopy(verilogSchemaComponent_wireLenType)
        elif (type == 1):
            resultBuild = copy.deepcopy(verilogSchemaComponent_regLenType)
        elif (type == 2):
            resultBuild = copy.deepcopy(verilogSchemaComponent_parameterLenType)
        elif (type == 3):
            resultBuild = copy.deepcopy(verilogSchemaComponent_localparamLenType)

    return resultBuild

def ioBuild(type, name, len):
    # name, len는 1개
    # input/output/output reg name; len <= 1
    # input/output/output reg [len-1:0] name; len > 1
    # 를 생성하는 함수

    keyword_content = name
    keyword_len = len

    if (len <= 1): 
        if (type == 0):
            resultBuild = copy.deepcopy(verilogSchemaComponent_inputType)
        elif (type == 1):
            resultBuild = copy.deepcopy(verilogSchemaComponent_outputType)
        elif (type == 2):
            resultBuild = copy.deepcopy(verilogSchemaComponent_outputregType)
    else:
        if (type == 0):
            resultBuild = copy.deepcopy(verilogSchemaComponent_inputLenType)
        elif (type == 1):
            resultBuild = copy.deepcopy(verilogSchemaComponent_outputLenType)
        elif (type == 2):
            resultBuild = copy.deepcopy(verilogSchemaComponent_outputregLenType)

    return resultBuild

def moduleBuild(name, io, content):
    # condition, content는 1개
    # module _name(_io);
    #   _content
    # endmodule
    # 를 생성하는 함수

    keyword_name = name
    keyword_field = io
    keyword_content = content

    resultBuild = copy.deepcopy(verilogSchema_module)

    return resultBuild

    # csv to FSM 
import csv
from collections import defaultdict

class csvFSMParser:
    def __init__(self):
        self.ports = []  # 포트 이름들
        self.port_types = []  # input/output/reg
        self.port_widths = []  # 비트 길이

        self.transitions = defaultdict(lambda: {"next_states": [], "conditions": []})
        self.register_ops = {}  # state: [op1, op2, ...]
        self.output_ops = {}    # state: [out1, out2, ...]

        self.internal_registers = []  # reg만 따로 저장 (port_types 기반)

    def parse_io_csv(self, filepath):
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 3:
                    continue
                name, port_type, width = row[0].strip(), row[1].strip(), row[2].strip()
                self.ports.append(name)
                self.port_types.append(port_type)
                self.port_widths.append(int(width))
                if port_type == "reg":
                    self.internal_registers.append(name)

    def parse_state_transition_csv(self, filepath):
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 3:
                    continue
                current_state = row[0].strip()
                next_state = row[1].strip()
                condition = row[2].strip() if row[2].strip() else ""
                self.transitions[current_state]["next_states"].append(next_state)
                self.transitions[current_state]["conditions"].append(condition)

    def parse_register_operation_csv(self, filepath):
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                state = row[0].strip()
                ops = [cell.strip() for cell in row[1:]]
                self.register_ops[state] = ops

    def parse_output_operation_csv(self, filepath):
        with open(filepath, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                state = row[0].strip()
                outputs = [cell.strip() for cell in row[1:]]
                self.output_ops[state] = outputs

    def summary(self):
        print("=== I/O & Register Definitions ===")
        for name, typ, width in zip(self.ports, self.port_types, self.port_widths):
            print(f"{name:10} | {typ:6} | {width}-bit")

        print("\n=== State Transitions ===")
        for state, trans in self.transitions.items():
            for next_state, cond in zip(trans["next_states"], trans["conditions"]):
                print(f"{state} -> {next_state}  if [{cond}]")

        print("\n=== Register Operations ===")
        for state, ops in self.register_ops.items():
            print(f"{state}: {ops}")

        print("\n=== Output Operations ===")
        for state, outs in self.output_ops.items():
            print(f"{state}: {outs}")

class FSMstructure:
    def __init__(self):
        self.ioList = ""
        self.ioContents = ""
        self.filpflops = ""
        self.