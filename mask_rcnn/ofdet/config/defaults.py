from .base_config import CfgNode as CN

_C = CN()

_C.DETECTOR = CN()
_C.DETECTOR.TYPE = ""
_C.DETECTOR.WEIGHT = ""

_C.DETECTOR.BACKBONE = CN()
_C.DETECTOR.BACKBONE.TYPE = ""
_C.DETECTOR.BACKBONE.DEPTH = 50
_C.DETECTOR.BACKBONE.FREEZE_STAGE = 2
_C.DETECTOR.BACKBONE.OUT_FEATURES = ["res2", "res3", "res4", "res5"]
_C.DETECTOR.BACKBONE.NUM_GROUPS = 1
_C.DETECTOR.BACKBONE.WIDTH_PER_GROUP = 64
_C.DETECTOR.BACKBONE.STEM_OUT_CHANNELS = 64
_C.DETECTOR.BACKBONE.RES2_OUT_CHANNELS = 256
_C.DETECTOR.BACKBONE.DARK2_OUT_CHANNELS = 64
_C.DETECTOR.BACKBONE.STRIDE_IN_1X1 = False
_C.DETECTOR.BACKBONE.RES5_DILATION = 1
_C.DETECTOR.BACKBONE.WEIGHT_DECAY = 0.0005

_C.DETECTOR.FPN = CN()
_C.DETECTOR.FPN.TYPE = ""
_C.DETECTOR.FPN.IN_FEATURES = ["res2", "res3", "res4", "res5"]
_C.DETECTOR.FPN.OUT_FEATURES = ["p2", "p3", "p4", "p5", "p6"]
_C.DETECTOR.FPN.START_IN_CHANNELS = 256
_C.DETECTOR.FPN.OUT_CHANNELS = [256]
_C.DETECTOR.FPN.BOTTLENECK_CHANNELS = []
_C.DETECTOR.FPN.LATERAL_NUM_BLOCKS = []
_C.DETECTOR.FPN.INPUT_CONV = False
_C.DETECTOR.FPN.SPP = False
_C.DETECTOR.FPN.WEIGHT_DECAY = 0.0005

_C.DETECTOR.FPN.TOP_BLOCK = CN()
_C.DETECTOR.FPN.TOP_BLOCK.TYPE = ""
_C.DETECTOR.FPN.TOP_BLOCK.IN_FEATURES = "p5"
_C.DETECTOR.FPN.TOP_BLOCK.OUT_CHANNELS = 256

_C.DETECTOR.RPN_HEAD = CN()
_C.DETECTOR.RPN_HEAD.TYPE = ""
_C.DETECTOR.RPN_HEAD.IN_CHANNELS = 256
_C.DETECTOR.RPN_HEAD.IN_FEATURES = ["p2", "p3", "p4", "p5", "p6"]
_C.DETECTOR.RPN_HEAD.BATCH_SIZE_PER_IMAGE = 256
_C.DETECTOR.RPN_HEAD.POSITIVE_FRACTION = 0.5
_C.DETECTOR.RPN_HEAD.PRE_NMS_TOPK_TRAIN = 2000
_C.DETECTOR.RPN_HEAD.PRE_NMS_TOPK_TEST = 1000
_C.DETECTOR.RPN_HEAD.POST_NMS_TOPK_TRAIN = 2000
_C.DETECTOR.RPN_HEAD.POST_NMS_TOPK_TEST = 1000
_C.DETECTOR.RPN_HEAD.NMS_THRESH = 0.7
_C.DETECTOR.RPN_HEAD.MIN_SIZE = 0.0
_C.DETECTOR.RPN_HEAD.BOUNDARY_THRESH = 0.0
_C.DETECTOR.RPN_HEAD.FG_IOU_THRESHOLD = 0.7
_C.DETECTOR.RPN_HEAD.BG_IOU_THRESHOLD = 0.3
_C.DETECTOR.RPN_HEAD.WEIGHT_DECAY = 0.0005

_C.DETECTOR.RPN_HEAD.ANCHOR_GENERATOR = CN()
_C.DETECTOR.RPN_HEAD.ANCHOR_GENERATOR.TYPE = "AnchorGenerator"
_C.DETECTOR.RPN_HEAD.ANCHOR_GENERATOR.SIZES = [32, 64, 128, 256, 512]
_C.DETECTOR.RPN_HEAD.ANCHOR_GENERATOR.ASPECT_RATIOS = [0.5, 1.0, 2.0]
_C.DETECTOR.RPN_HEAD.ANCHOR_GENERATOR.STRIDES = [4, 8, 16, 32, 64]

_C.DETECTOR.DENSE_HEAD = CN()
_C.DETECTOR.DENSE_HEAD.TYPE = ""
_C.DETECTOR.DENSE_HEAD.IN_FEATURES = ["p3", "p4", "p5", "p6", "p7"]
_C.DETECTOR.DENSE_HEAD.NUM_CLASSES = 80
_C.DETECTOR.DENSE_HEAD.PRE_NMS_TOPK = 1000
_C.DETECTOR.DENSE_HEAD.SCORE_THRESH = 0.05
_C.DETECTOR.DENSE_HEAD.NMS_THRESH = 0.5
_C.DETECTOR.DENSE_HEAD.NUM_CONV = 4
_C.DETECTOR.DENSE_HEAD.CONV_DIM = 256
_C.DETECTOR.DENSE_HEAD.DETECTIONS_PER_IMG = 100
_C.DETECTOR.DENSE_HEAD.WEIGHT_DECAY = 0.0005

_C.DETECTOR.DENSE_HEAD.ANCHOR_GENERATOR = CN()
_C.DETECTOR.DENSE_HEAD.ANCHOR_GENERATOR.TYPE = "AnchorGenerator"
_C.DETECTOR.DENSE_HEAD.ANCHOR_GENERATOR.SIZES = [32, 64, 128, 256, 512]
_C.DETECTOR.DENSE_HEAD.ANCHOR_GENERATOR.ASPECT_RATIOS = [0.5, 1.0, 2.0]
_C.DETECTOR.DENSE_HEAD.ANCHOR_GENERATOR.STRIDES = [4, 8, 16, 32, 64]

_C.DETECTOR.ROI_HEAD = CN()
_C.DETECTOR.ROI_HEAD.TYPE = ""
_C.DETECTOR.ROI_HEAD.IN_FEATURES = ["p2", "p3", "p4", "p5"]
_C.DETECTOR.ROI_HEAD.NUM_CLASSES = 81
_C.DETECTOR.ROI_HEAD.BBOX_REG_WEIGHTS = (10.0, 10.0, 5.0, 5.0)
_C.DETECTOR.ROI_HEAD.SCORE_THRESH = 0.05
_C.DETECTOR.ROI_HEAD.NMS_THRESH = 0.5
_C.DETECTOR.ROI_HEAD.DETECTIONS_PER_IMG = 100

_C.DETECTOR.ROI_HEAD.BOX_HEAD = CN()
_C.DETECTOR.ROI_HEAD.BOX_HEAD.TYPE = ""
_C.DETECTOR.ROI_HEAD.BOX_HEAD.POOLER_RESOLUTION = 7
_C.DETECTOR.ROI_HEAD.BOX_HEAD.POOLER_SAMPLING_RATIO = 2
_C.DETECTOR.ROI_HEAD.BOX_HEAD.POOLER_SCALES = (0.25, 0.125, 0.0625, 0.03125)
_C.DETECTOR.ROI_HEAD.BOX_HEAD.NUM_CONV = 0
_C.DETECTOR.ROI_HEAD.BOX_HEAD.CONV_DIM = 256
_C.DETECTOR.ROI_HEAD.BOX_HEAD.NUM_FC = 2
_C.DETECTOR.ROI_HEAD.BOX_HEAD.FC_DIM = 1024
_C.DETECTOR.ROI_HEAD.BOX_HEAD.NUM_CLASSES = 81
_C.DETECTOR.ROI_HEAD.BOX_HEAD.CLS_AGNOSTIC_BBOX_REG = False
_C.DETECTOR.ROI_HEAD.BOX_HEAD.WITH_AVG_POOL = False
_C.DETECTOR.ROI_HEAD.BOX_HEAD.WEIGHT_DECAY = 0.0005

_C.DETECTOR.ROI_HEAD.MASK_HEAD = CN()
_C.DETECTOR.ROI_HEAD.MASK_HEAD.TYPE = ""
_C.DETECTOR.ROI_HEAD.MASK_HEAD.IN_CHANNELS = 256
_C.DETECTOR.ROI_HEAD.MASK_HEAD.OUT_CHANNELS = 256
_C.DETECTOR.ROI_HEAD.MASK_HEAD.POOLER_RESOLUTION = 14
_C.DETECTOR.ROI_HEAD.MASK_HEAD.POOLER_SAMPLING_RATIO = 2
_C.DETECTOR.ROI_HEAD.MASK_HEAD.POOLER_SCALES = (0.25, 0.125, 0.0625, 0.03125)
_C.DETECTOR.ROI_HEAD.MASK_HEAD.WITH_CONV_RES = []
_C.DETECTOR.ROI_HEAD.MASK_HEAD.NUM_CONV = 4
_C.DETECTOR.ROI_HEAD.MASK_HEAD.CONV_DIM = 256
_C.DETECTOR.ROI_HEAD.MASK_HEAD.NUM_CLASSES = 81
_C.DETECTOR.ROI_HEAD.MASK_HEAD.WEIGHT_DECAY = 0.0005

_C.DETECTOR.ROI_HEAD.SHARED_HEAD = CN()
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.TYPE = ""
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.DEPTH = 50
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.STAGE = 3
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.NUM_GROUPS = 1
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.WIDTH_PER_GROUP = 64
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.RES2_OUT_CHANNELS = 256
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.STRIDE_IN_1X1 = True
_C.DETECTOR.ROI_HEAD.SHARED_HEAD.WEIGHT_DECAY = 0.0005

_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD = CN()
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.TYPE = ""
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.POOLER_RESOLUTION = 14
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.POOLER_SAMPLING_RATIO = 0
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.POOLER_SCALES = (0.125,)
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.IN_FEATURES = ["p2", "p3", "p4", "p5"]
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.FUSION_LEVEL = "p3"
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.FUSE_CONV_DIM = 256
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.NUM_CONV = 4
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.CONV_DIM = 256
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.NUM_CLASSES = 183
_C.DETECTOR.ROI_HEAD.SEMANTIC_HEAD.WEIGHT_DECAY = 0.0005

_C.ENV = CN()
_C.ENV.NUM_GPUS = 1
_C.ENV.CUDNN_BUFFER_SIZE_LIMIT = 1024
_C.DTYPE = "float32"

_C.DATASETS = CN()
_C.DATASETS.TEST = "/dataset/mscoco_2017"
_C.DATASETS.IMAGE_DIR_TEST = "val2017"
_C.DATASETS.ANNOTATION_TEST = "annotations/instances_val2017.json"

_C.INPUT = CN()
_C.INPUT.MIN_SIZE_TEST = 800
_C.INPUT.MAX_SIZE_TEST = 1333
_C.INPUT.PIXEL_MEAN = [102.9801, 115.9465, 122.7717]
_C.INPUT.PIXEL_STD = [1.0, 1.0, 1.0]
_C.INPUT.COLOR_SPACE = "BGR"
_C.INPUT.SIZE_DIVISIBILITY = 32

_C.TEST = CN()
_C.TEST.IMS_PER_BATCH = 1

_C.OUTPUT_DIR = "./output"


def get_default_cfgs():
    """
    Get a yacs CfgNode object with default values for maskrcnn object
    """
    return _C.clone()
