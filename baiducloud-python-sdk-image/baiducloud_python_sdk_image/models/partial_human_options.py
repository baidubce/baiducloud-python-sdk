"""
PartialHumanOptions information
"""

from baiducloud_python_sdk_core.abstract_model import AbstractModel


class PartialHumanOptions(AbstractModel):
    """
    PartialHumanOptions
    """

    def __init__(
        self,
        body_smooth_highpass=None,
        eye_width_right=None,
        skin_red=None,
        nose_scale=None,
        makeup_eyelash_id=None,
        remove_eye_streaks=None,
        ai_body_flow_thin=None,
        jaw_width_left=None,
        cheekbone_width_left=None,
        face_color_same=None,
        face_small=None,
        remove_forehead_wrinkles=None,
        eye_scale_same=None,
        makeup_shadow=None,
        makeup_eyebrow=None,
        makeup_blush=None,
        makeup_lipstick=None,
        leg_thin=None,
        remove_double_chin=None,
        face_symmetry=None,
        eye_height=None,
        eye_width=None,
        remove_burst_hair_body=None,
        face_smooth_new=None,
        remove_body_flaw=None,
        teeth_white_add_bright=None,
        neck_thin=None,
        hairline_height=None,
        right_eyebrow_enhance=None,
        remove_face_glossy=None,
        clothes_flaw_remove=None,
        fill_hair_part=None,
        makeup_eyeball_id=None,
        remove_lip_wrinkles=None,
        shiny_eye=None,
        makeup_eyebrow_id=None,
        nose_height=None,
        lip_plump_up=None,
        face_thin=None,
        head_small=None,
        skin_prefer=None,
        remove_white_hair=None,
        eye_position=None,
        face_smooth_gray=None,
        skin_white=None,
        forehead_height=None,
        eye_scale=None,
        eyebrow_distance=None,
        eye_height_left=None,
        eye_width_left=None,
        remove_dark_circles=None,
        makeup_freckle_id=None,
        jaw_width=None,
        cheekbone_width_right=None,
        left_eyebrow_enhance=None,
        body_smooth_fine=None,
        body_color_same=None,
        remove_glasses_reflection=None,
        makeup_highlight=None,
        remove_polymastia=None,
        eye_distance_right=None,
        mouth_scale=None,
        mouth_position=None,
        chin_height=None,
        eye_height_right=None,
        makeup_face_id=None,
        body_smooth=None,
        skin_color=None,
        face_v=None,
        eye_angle_right=None,
        lip_plump_down=None,
        face_width=None,
        eye_position_left=None,
        eye_position_right=None,
        neck_length=None,
        face_shadow=None,
        skin_bright=None,
        skin_color_id=None,
        nose_bridge=None,
        nose_tip=None,
        left_swan_neck=None,
        face_smooth_highpass=None,
        eye_scale_right=None,
        remove_face_flaw=None,
        mouth_width=None,
        face_smooth_lowpass=None,
        remove_burst_hair=None,
        makeup_eye_shadow_id=None,
        body_smooth_lowpass=None,
        eye_angle=None,
        ai_body_thin=None,
        makeup_eyelash=None,
        makeup_face=None,
        nose_wing=None,
        teeth_white=None,
        body_thin=None,
        skin_sharpen=None,
        eye_scale_left=None,
        remove_neck_wrinkles=None,
        calvaria_height=None,
        jaw_width_right=None,
        waist_thin=None,
        face_highlight=None,
        remove_eye_around_wrinkles=None,
        eyebrow_thickness=None,
        teeth_repair=None,
        right_swan_neck=None,
        arm_thin=None,
        makeup_eyeball=None,
        cheekbone_width=None,
        eye_angle_left=None,
        eye_distance_left=None,
        makeup_eye_shadow=None,
        teeth_white_des_yellow=None,
        face_smooth_fine=None,
        makeup_freckle=None,
        makeup_blush_id=None,
        remove_laugh_line=None,
        makeup_lipstick_id=None,
        face_smooth=None,
        eyebrow_height=None,
        eye_distance=None,
        remove_face_moles=None,
        remove_stretch_mark=None,
        remove_burst_hair_back=None,
    ):
        """
        Initialize PartialHumanOptions instance.

        :param body_smooth_highpass:
        :type body_smooth_highpass: float (optional)

        :param eye_width_right:
        :type eye_width_right: float (optional)

        :param skin_red:
        :type skin_red: float (optional)

        :param nose_scale:
        :type nose_scale: float (optional)

        :param makeup_eyelash_id:
        :type makeup_eyelash_id: int (optional)

        :param remove_eye_streaks:
        :type remove_eye_streaks: float (optional)

        :param ai_body_flow_thin:
        :type ai_body_flow_thin: float (optional)

        :param jaw_width_left:
        :type jaw_width_left: float (optional)

        :param cheekbone_width_left:
        :type cheekbone_width_left: float (optional)

        :param face_color_same:
        :type face_color_same: float (optional)

        :param face_small:
        :type face_small: float (optional)

        :param remove_forehead_wrinkles:
        :type remove_forehead_wrinkles: float (optional)

        :param eye_scale_same:
        :type eye_scale_same: bool (optional)

        :param makeup_shadow:
        :type makeup_shadow: float (optional)

        :param makeup_eyebrow:
        :type makeup_eyebrow: float (optional)

        :param makeup_blush:
        :type makeup_blush: float (optional)

        :param makeup_lipstick:
        :type makeup_lipstick: float (optional)

        :param leg_thin:
        :type leg_thin: float (optional)

        :param remove_double_chin:
        :type remove_double_chin: float (optional)

        :param face_symmetry:
        :type face_symmetry: float (optional)

        :param eye_height:
        :type eye_height: float (optional)

        :param eye_width:
        :type eye_width: float (optional)

        :param remove_burst_hair_body:
        :type remove_burst_hair_body: float (optional)

        :param face_smooth_new:
        :type face_smooth_new: float (optional)

        :param remove_body_flaw:
        :type remove_body_flaw: float (optional)

        :param teeth_white_add_bright:
        :type teeth_white_add_bright: float (optional)

        :param neck_thin:
        :type neck_thin: float (optional)

        :param hairline_height:
        :type hairline_height: float (optional)

        :param right_eyebrow_enhance:
        :type right_eyebrow_enhance: float (optional)

        :param remove_face_glossy:
        :type remove_face_glossy: float (optional)

        :param clothes_flaw_remove:
        :type clothes_flaw_remove: float (optional)

        :param fill_hair_part:
        :type fill_hair_part: float (optional)

        :param makeup_eyeball_id:
        :type makeup_eyeball_id: int (optional)

        :param remove_lip_wrinkles:
        :type remove_lip_wrinkles: float (optional)

        :param shiny_eye:
        :type shiny_eye: float (optional)

        :param makeup_eyebrow_id:
        :type makeup_eyebrow_id: int (optional)

        :param nose_height:
        :type nose_height: float (optional)

        :param lip_plump_up:
        :type lip_plump_up: float (optional)

        :param face_thin:
        :type face_thin: float (optional)

        :param head_small:
        :type head_small: float (optional)

        :param skin_prefer:
        :type skin_prefer: float (optional)

        :param remove_white_hair:
        :type remove_white_hair: float (optional)

        :param eye_position:
        :type eye_position: float (optional)

        :param face_smooth_gray:
        :type face_smooth_gray: float (optional)

        :param skin_white:
        :type skin_white: float (optional)

        :param forehead_height:
        :type forehead_height: float (optional)

        :param eye_scale:
        :type eye_scale: float (optional)

        :param eyebrow_distance:
        :type eyebrow_distance: float (optional)

        :param eye_height_left:
        :type eye_height_left: float (optional)

        :param eye_width_left:
        :type eye_width_left: float (optional)

        :param remove_dark_circles:
        :type remove_dark_circles: float (optional)

        :param makeup_freckle_id:
        :type makeup_freckle_id: int (optional)

        :param jaw_width:
        :type jaw_width: float (optional)

        :param cheekbone_width_right:
        :type cheekbone_width_right: float (optional)

        :param left_eyebrow_enhance:
        :type left_eyebrow_enhance: float (optional)

        :param body_smooth_fine:
        :type body_smooth_fine: float (optional)

        :param body_color_same:
        :type body_color_same: float (optional)

        :param remove_glasses_reflection:
        :type remove_glasses_reflection: float (optional)

        :param makeup_highlight:
        :type makeup_highlight: float (optional)

        :param remove_polymastia:
        :type remove_polymastia: int (optional)

        :param eye_distance_right:
        :type eye_distance_right: float (optional)

        :param mouth_scale:
        :type mouth_scale: float (optional)

        :param mouth_position:
        :type mouth_position: float (optional)

        :param chin_height:
        :type chin_height: float (optional)

        :param eye_height_right:
        :type eye_height_right: float (optional)

        :param makeup_face_id:
        :type makeup_face_id: int (optional)

        :param body_smooth:
        :type body_smooth: float (optional)

        :param skin_color:
        :type skin_color: float (optional)

        :param face_v:
        :type face_v: float (optional)

        :param eye_angle_right:
        :type eye_angle_right: float (optional)

        :param lip_plump_down:
        :type lip_plump_down: float (optional)

        :param face_width:
        :type face_width: float (optional)

        :param eye_position_left:
        :type eye_position_left: float (optional)

        :param eye_position_right:
        :type eye_position_right: float (optional)

        :param neck_length:
        :type neck_length: float (optional)

        :param face_shadow:
        :type face_shadow: float (optional)

        :param skin_bright:
        :type skin_bright: float (optional)

        :param skin_color_id:
        :type skin_color_id: int (optional)

        :param nose_bridge:
        :type nose_bridge: float (optional)

        :param nose_tip:
        :type nose_tip: float (optional)

        :param left_swan_neck:
        :type left_swan_neck: float (optional)

        :param face_smooth_highpass:
        :type face_smooth_highpass: float (optional)

        :param eye_scale_right:
        :type eye_scale_right: float (optional)

        :param remove_face_flaw:
        :type remove_face_flaw: float (optional)

        :param mouth_width:
        :type mouth_width: float (optional)

        :param face_smooth_lowpass:
        :type face_smooth_lowpass: float (optional)

        :param remove_burst_hair:
        :type remove_burst_hair: float (optional)

        :param makeup_eye_shadow_id:
        :type makeup_eye_shadow_id: int (optional)

        :param body_smooth_lowpass:
        :type body_smooth_lowpass: float (optional)

        :param eye_angle:
        :type eye_angle: float (optional)

        :param ai_body_thin:
        :type ai_body_thin: float (optional)

        :param makeup_eyelash:
        :type makeup_eyelash: float (optional)

        :param makeup_face:
        :type makeup_face: float (optional)

        :param nose_wing:
        :type nose_wing: float (optional)

        :param teeth_white:
        :type teeth_white: float (optional)

        :param body_thin:
        :type body_thin: float (optional)

        :param skin_sharpen:
        :type skin_sharpen: float (optional)

        :param eye_scale_left:
        :type eye_scale_left: float (optional)

        :param remove_neck_wrinkles:
        :type remove_neck_wrinkles: float (optional)

        :param calvaria_height:
        :type calvaria_height: float (optional)

        :param jaw_width_right:
        :type jaw_width_right: float (optional)

        :param waist_thin:
        :type waist_thin: float (optional)

        :param face_highlight:
        :type face_highlight: float (optional)

        :param remove_eye_around_wrinkles:
        :type remove_eye_around_wrinkles: float (optional)

        :param eyebrow_thickness:
        :type eyebrow_thickness: float (optional)

        :param teeth_repair:
        :type teeth_repair: int (optional)

        :param right_swan_neck:
        :type right_swan_neck: float (optional)

        :param arm_thin:
        :type arm_thin: float (optional)

        :param makeup_eyeball:
        :type makeup_eyeball: float (optional)

        :param cheekbone_width:
        :type cheekbone_width: float (optional)

        :param eye_angle_left:
        :type eye_angle_left: float (optional)

        :param eye_distance_left:
        :type eye_distance_left: float (optional)

        :param makeup_eye_shadow:
        :type makeup_eye_shadow: float (optional)

        :param teeth_white_des_yellow:
        :type teeth_white_des_yellow: float (optional)

        :param face_smooth_fine:
        :type face_smooth_fine: float (optional)

        :param makeup_freckle:
        :type makeup_freckle: float (optional)

        :param makeup_blush_id:
        :type makeup_blush_id: int (optional)

        :param remove_laugh_line:
        :type remove_laugh_line: float (optional)

        :param makeup_lipstick_id:
        :type makeup_lipstick_id: int (optional)

        :param face_smooth:
        :type face_smooth: float (optional)

        :param eyebrow_height:
        :type eyebrow_height: float (optional)

        :param eye_distance:
        :type eye_distance: float (optional)

        :param remove_face_moles:
        :type remove_face_moles: int (optional)

        :param remove_stretch_mark:
        :type remove_stretch_mark: float (optional)

        :param remove_burst_hair_back:
        :type remove_burst_hair_back: float (optional)
        """
        super().__init__()
        self.body_smooth_highpass = body_smooth_highpass
        self.eye_width_right = eye_width_right
        self.skin_red = skin_red
        self.nose_scale = nose_scale
        self.makeup_eyelash_id = makeup_eyelash_id
        self.remove_eye_streaks = remove_eye_streaks
        self.ai_body_flow_thin = ai_body_flow_thin
        self.jaw_width_left = jaw_width_left
        self.cheekbone_width_left = cheekbone_width_left
        self.face_color_same = face_color_same
        self.face_small = face_small
        self.remove_forehead_wrinkles = remove_forehead_wrinkles
        self.eye_scale_same = eye_scale_same
        self.makeup_shadow = makeup_shadow
        self.makeup_eyebrow = makeup_eyebrow
        self.makeup_blush = makeup_blush
        self.makeup_lipstick = makeup_lipstick
        self.leg_thin = leg_thin
        self.remove_double_chin = remove_double_chin
        self.face_symmetry = face_symmetry
        self.eye_height = eye_height
        self.eye_width = eye_width
        self.remove_burst_hair_body = remove_burst_hair_body
        self.face_smooth_new = face_smooth_new
        self.remove_body_flaw = remove_body_flaw
        self.teeth_white_add_bright = teeth_white_add_bright
        self.neck_thin = neck_thin
        self.hairline_height = hairline_height
        self.right_eyebrow_enhance = right_eyebrow_enhance
        self.remove_face_glossy = remove_face_glossy
        self.clothes_flaw_remove = clothes_flaw_remove
        self.fill_hair_part = fill_hair_part
        self.makeup_eyeball_id = makeup_eyeball_id
        self.remove_lip_wrinkles = remove_lip_wrinkles
        self.shiny_eye = shiny_eye
        self.makeup_eyebrow_id = makeup_eyebrow_id
        self.nose_height = nose_height
        self.lip_plump_up = lip_plump_up
        self.face_thin = face_thin
        self.head_small = head_small
        self.skin_prefer = skin_prefer
        self.remove_white_hair = remove_white_hair
        self.eye_position = eye_position
        self.face_smooth_gray = face_smooth_gray
        self.skin_white = skin_white
        self.forehead_height = forehead_height
        self.eye_scale = eye_scale
        self.eyebrow_distance = eyebrow_distance
        self.eye_height_left = eye_height_left
        self.eye_width_left = eye_width_left
        self.remove_dark_circles = remove_dark_circles
        self.makeup_freckle_id = makeup_freckle_id
        self.jaw_width = jaw_width
        self.cheekbone_width_right = cheekbone_width_right
        self.left_eyebrow_enhance = left_eyebrow_enhance
        self.body_smooth_fine = body_smooth_fine
        self.body_color_same = body_color_same
        self.remove_glasses_reflection = remove_glasses_reflection
        self.makeup_highlight = makeup_highlight
        self.remove_polymastia = remove_polymastia
        self.eye_distance_right = eye_distance_right
        self.mouth_scale = mouth_scale
        self.mouth_position = mouth_position
        self.chin_height = chin_height
        self.eye_height_right = eye_height_right
        self.makeup_face_id = makeup_face_id
        self.body_smooth = body_smooth
        self.skin_color = skin_color
        self.face_v = face_v
        self.eye_angle_right = eye_angle_right
        self.lip_plump_down = lip_plump_down
        self.face_width = face_width
        self.eye_position_left = eye_position_left
        self.eye_position_right = eye_position_right
        self.neck_length = neck_length
        self.face_shadow = face_shadow
        self.skin_bright = skin_bright
        self.skin_color_id = skin_color_id
        self.nose_bridge = nose_bridge
        self.nose_tip = nose_tip
        self.left_swan_neck = left_swan_neck
        self.face_smooth_highpass = face_smooth_highpass
        self.eye_scale_right = eye_scale_right
        self.remove_face_flaw = remove_face_flaw
        self.mouth_width = mouth_width
        self.face_smooth_lowpass = face_smooth_lowpass
        self.remove_burst_hair = remove_burst_hair
        self.makeup_eye_shadow_id = makeup_eye_shadow_id
        self.body_smooth_lowpass = body_smooth_lowpass
        self.eye_angle = eye_angle
        self.ai_body_thin = ai_body_thin
        self.makeup_eyelash = makeup_eyelash
        self.makeup_face = makeup_face
        self.nose_wing = nose_wing
        self.teeth_white = teeth_white
        self.body_thin = body_thin
        self.skin_sharpen = skin_sharpen
        self.eye_scale_left = eye_scale_left
        self.remove_neck_wrinkles = remove_neck_wrinkles
        self.calvaria_height = calvaria_height
        self.jaw_width_right = jaw_width_right
        self.waist_thin = waist_thin
        self.face_highlight = face_highlight
        self.remove_eye_around_wrinkles = remove_eye_around_wrinkles
        self.eyebrow_thickness = eyebrow_thickness
        self.teeth_repair = teeth_repair
        self.right_swan_neck = right_swan_neck
        self.arm_thin = arm_thin
        self.makeup_eyeball = makeup_eyeball
        self.cheekbone_width = cheekbone_width
        self.eye_angle_left = eye_angle_left
        self.eye_distance_left = eye_distance_left
        self.makeup_eye_shadow = makeup_eye_shadow
        self.teeth_white_des_yellow = teeth_white_des_yellow
        self.face_smooth_fine = face_smooth_fine
        self.makeup_freckle = makeup_freckle
        self.makeup_blush_id = makeup_blush_id
        self.remove_laugh_line = remove_laugh_line
        self.makeup_lipstick_id = makeup_lipstick_id
        self.face_smooth = face_smooth
        self.eyebrow_height = eyebrow_height
        self.eye_distance = eye_distance
        self.remove_face_moles = remove_face_moles
        self.remove_stretch_mark = remove_stretch_mark
        self.remove_burst_hair_back = remove_burst_hair_back

    def to_dict(self):
        """
        Convert the model instance to a dictionary representation.

        Nested model objects are recursively converted to dictionaries.

        :return: Dictionary representation of the model
        :rtype: dict
        """
        _map = super().to_dict()
        if _map is not None:
            return _map
        result = dict()
        if self.body_smooth_highpass is not None:
            result['body_smooth_highpass'] = self.body_smooth_highpass
        if self.eye_width_right is not None:
            result['eye_width_right'] = self.eye_width_right
        if self.skin_red is not None:
            result['skin_red'] = self.skin_red
        if self.nose_scale is not None:
            result['nose_scale'] = self.nose_scale
        if self.makeup_eyelash_id is not None:
            result['makeup_eyelash_id'] = self.makeup_eyelash_id
        if self.remove_eye_streaks is not None:
            result['remove_eye_streaks'] = self.remove_eye_streaks
        if self.ai_body_flow_thin is not None:
            result['ai_body_flow_thin'] = self.ai_body_flow_thin
        if self.jaw_width_left is not None:
            result['jaw_width_left'] = self.jaw_width_left
        if self.cheekbone_width_left is not None:
            result['cheekbone_width_left'] = self.cheekbone_width_left
        if self.face_color_same is not None:
            result['face_color_same'] = self.face_color_same
        if self.face_small is not None:
            result['face_small'] = self.face_small
        if self.remove_forehead_wrinkles is not None:
            result['remove_forehead_wrinkles'] = self.remove_forehead_wrinkles
        if self.eye_scale_same is not None:
            result['eye_scale_same'] = self.eye_scale_same
        if self.makeup_shadow is not None:
            result['makeup_shadow'] = self.makeup_shadow
        if self.makeup_eyebrow is not None:
            result['makeup_eyebrow'] = self.makeup_eyebrow
        if self.makeup_blush is not None:
            result['makeup_blush'] = self.makeup_blush
        if self.makeup_lipstick is not None:
            result['makeup_lipstick'] = self.makeup_lipstick
        if self.leg_thin is not None:
            result['leg_thin'] = self.leg_thin
        if self.remove_double_chin is not None:
            result['remove_double_chin'] = self.remove_double_chin
        if self.face_symmetry is not None:
            result['face_symmetry'] = self.face_symmetry
        if self.eye_height is not None:
            result['eye_height'] = self.eye_height
        if self.eye_width is not None:
            result['eye_width'] = self.eye_width
        if self.remove_burst_hair_body is not None:
            result['remove_burst_hair_body'] = self.remove_burst_hair_body
        if self.face_smooth_new is not None:
            result['face_smooth_new'] = self.face_smooth_new
        if self.remove_body_flaw is not None:
            result['remove_body_flaw'] = self.remove_body_flaw
        if self.teeth_white_add_bright is not None:
            result['teeth_white_add_bright'] = self.teeth_white_add_bright
        if self.neck_thin is not None:
            result['neck_thin'] = self.neck_thin
        if self.hairline_height is not None:
            result['hairline_height'] = self.hairline_height
        if self.right_eyebrow_enhance is not None:
            result['right_eyebrow_enhance'] = self.right_eyebrow_enhance
        if self.remove_face_glossy is not None:
            result['remove_face_glossy'] = self.remove_face_glossy
        if self.clothes_flaw_remove is not None:
            result['clothes_flaw_remove'] = self.clothes_flaw_remove
        if self.fill_hair_part is not None:
            result['fill_hair_part'] = self.fill_hair_part
        if self.makeup_eyeball_id is not None:
            result['makeup_eyeball_id'] = self.makeup_eyeball_id
        if self.remove_lip_wrinkles is not None:
            result['remove_lip_wrinkles'] = self.remove_lip_wrinkles
        if self.shiny_eye is not None:
            result['shiny_eye'] = self.shiny_eye
        if self.makeup_eyebrow_id is not None:
            result['makeup_eyebrow_id'] = self.makeup_eyebrow_id
        if self.nose_height is not None:
            result['nose_height'] = self.nose_height
        if self.lip_plump_up is not None:
            result['lip_plump_up'] = self.lip_plump_up
        if self.face_thin is not None:
            result['face_thin'] = self.face_thin
        if self.head_small is not None:
            result['head_small'] = self.head_small
        if self.skin_prefer is not None:
            result['skin_prefer'] = self.skin_prefer
        if self.remove_white_hair is not None:
            result['remove_white_hair'] = self.remove_white_hair
        if self.eye_position is not None:
            result['eye_position'] = self.eye_position
        if self.face_smooth_gray is not None:
            result['face_smooth_gray'] = self.face_smooth_gray
        if self.skin_white is not None:
            result['skin_white'] = self.skin_white
        if self.forehead_height is not None:
            result['forehead_height'] = self.forehead_height
        if self.eye_scale is not None:
            result['eye_scale'] = self.eye_scale
        if self.eyebrow_distance is not None:
            result['eyebrow_distance'] = self.eyebrow_distance
        if self.eye_height_left is not None:
            result['eye_height_left'] = self.eye_height_left
        if self.eye_width_left is not None:
            result['eye_width_left'] = self.eye_width_left
        if self.remove_dark_circles is not None:
            result['remove_dark_circles'] = self.remove_dark_circles
        if self.makeup_freckle_id is not None:
            result['makeup_freckle_id'] = self.makeup_freckle_id
        if self.jaw_width is not None:
            result['jaw_width'] = self.jaw_width
        if self.cheekbone_width_right is not None:
            result['cheekbone_width_right'] = self.cheekbone_width_right
        if self.left_eyebrow_enhance is not None:
            result['left_eyebrow_enhance'] = self.left_eyebrow_enhance
        if self.body_smooth_fine is not None:
            result['body_smooth_fine'] = self.body_smooth_fine
        if self.body_color_same is not None:
            result['body_color_same'] = self.body_color_same
        if self.remove_glasses_reflection is not None:
            result['remove_glasses_reflection'] = self.remove_glasses_reflection
        if self.makeup_highlight is not None:
            result['makeup_highlight'] = self.makeup_highlight
        if self.remove_polymastia is not None:
            result['remove_polymastia'] = self.remove_polymastia
        if self.eye_distance_right is not None:
            result['eye_distance_right'] = self.eye_distance_right
        if self.mouth_scale is not None:
            result['mouth_scale'] = self.mouth_scale
        if self.mouth_position is not None:
            result['mouth_position'] = self.mouth_position
        if self.chin_height is not None:
            result['chin_height'] = self.chin_height
        if self.eye_height_right is not None:
            result['eye_height_right'] = self.eye_height_right
        if self.makeup_face_id is not None:
            result['makeup_face_id'] = self.makeup_face_id
        if self.body_smooth is not None:
            result['body_smooth'] = self.body_smooth
        if self.skin_color is not None:
            result['skin_color'] = self.skin_color
        if self.face_v is not None:
            result['face_v'] = self.face_v
        if self.eye_angle_right is not None:
            result['eye_angle_right'] = self.eye_angle_right
        if self.lip_plump_down is not None:
            result['lip_plump_down'] = self.lip_plump_down
        if self.face_width is not None:
            result['face_width'] = self.face_width
        if self.eye_position_left is not None:
            result['eye_position_left'] = self.eye_position_left
        if self.eye_position_right is not None:
            result['eye_position_right'] = self.eye_position_right
        if self.neck_length is not None:
            result['neck_length'] = self.neck_length
        if self.face_shadow is not None:
            result['face_shadow'] = self.face_shadow
        if self.skin_bright is not None:
            result['skin_bright'] = self.skin_bright
        if self.skin_color_id is not None:
            result['skin_color_id'] = self.skin_color_id
        if self.nose_bridge is not None:
            result['nose_bridge'] = self.nose_bridge
        if self.nose_tip is not None:
            result['nose_tip'] = self.nose_tip
        if self.left_swan_neck is not None:
            result['left_swan_neck'] = self.left_swan_neck
        if self.face_smooth_highpass is not None:
            result['face_smooth_highpass'] = self.face_smooth_highpass
        if self.eye_scale_right is not None:
            result['eye_scale_right'] = self.eye_scale_right
        if self.remove_face_flaw is not None:
            result['remove_face_flaw'] = self.remove_face_flaw
        if self.mouth_width is not None:
            result['mouth_width'] = self.mouth_width
        if self.face_smooth_lowpass is not None:
            result['face_smooth_lowpass'] = self.face_smooth_lowpass
        if self.remove_burst_hair is not None:
            result['remove_burst_hair'] = self.remove_burst_hair
        if self.makeup_eye_shadow_id is not None:
            result['makeup_eye_shadow_id'] = self.makeup_eye_shadow_id
        if self.body_smooth_lowpass is not None:
            result['body_smooth_lowpass'] = self.body_smooth_lowpass
        if self.eye_angle is not None:
            result['eye_angle'] = self.eye_angle
        if self.ai_body_thin is not None:
            result['ai_body_thin'] = self.ai_body_thin
        if self.makeup_eyelash is not None:
            result['makeup_eyelash'] = self.makeup_eyelash
        if self.makeup_face is not None:
            result['makeup_face'] = self.makeup_face
        if self.nose_wing is not None:
            result['nose_wing'] = self.nose_wing
        if self.teeth_white is not None:
            result['teeth_white'] = self.teeth_white
        if self.body_thin is not None:
            result['body_thin'] = self.body_thin
        if self.skin_sharpen is not None:
            result['skin_sharpen'] = self.skin_sharpen
        if self.eye_scale_left is not None:
            result['eye_scale_left'] = self.eye_scale_left
        if self.remove_neck_wrinkles is not None:
            result['remove_neck_wrinkles'] = self.remove_neck_wrinkles
        if self.calvaria_height is not None:
            result['calvaria_height'] = self.calvaria_height
        if self.jaw_width_right is not None:
            result['jaw_width_right'] = self.jaw_width_right
        if self.waist_thin is not None:
            result['waist_thin'] = self.waist_thin
        if self.face_highlight is not None:
            result['face_highlight'] = self.face_highlight
        if self.remove_eye_around_wrinkles is not None:
            result['remove_eye_around_wrinkles'] = self.remove_eye_around_wrinkles
        if self.eyebrow_thickness is not None:
            result['eyebrow_thickness'] = self.eyebrow_thickness
        if self.teeth_repair is not None:
            result['teeth_repair'] = self.teeth_repair
        if self.right_swan_neck is not None:
            result['right_swan_neck'] = self.right_swan_neck
        if self.arm_thin is not None:
            result['arm_thin'] = self.arm_thin
        if self.makeup_eyeball is not None:
            result['makeup_eyeball'] = self.makeup_eyeball
        if self.cheekbone_width is not None:
            result['cheekbone_width'] = self.cheekbone_width
        if self.eye_angle_left is not None:
            result['eye_angle_left'] = self.eye_angle_left
        if self.eye_distance_left is not None:
            result['eye_distance_left'] = self.eye_distance_left
        if self.makeup_eye_shadow is not None:
            result['makeup_eye_shadow'] = self.makeup_eye_shadow
        if self.teeth_white_des_yellow is not None:
            result['teeth_white_des_yellow'] = self.teeth_white_des_yellow
        if self.face_smooth_fine is not None:
            result['face_smooth_fine'] = self.face_smooth_fine
        if self.makeup_freckle is not None:
            result['makeup_freckle'] = self.makeup_freckle
        if self.makeup_blush_id is not None:
            result['makeup_blush_id'] = self.makeup_blush_id
        if self.remove_laugh_line is not None:
            result['remove_laugh_line'] = self.remove_laugh_line
        if self.makeup_lipstick_id is not None:
            result['makeup_lipstick_id'] = self.makeup_lipstick_id
        if self.face_smooth is not None:
            result['face_smooth'] = self.face_smooth
        if self.eyebrow_height is not None:
            result['eyebrow_height'] = self.eyebrow_height
        if self.eye_distance is not None:
            result['eye_distance'] = self.eye_distance
        if self.remove_face_moles is not None:
            result['remove_face_moles'] = self.remove_face_moles
        if self.remove_stretch_mark is not None:
            result['remove_stretch_mark'] = self.remove_stretch_mark
        if self.remove_burst_hair_back is not None:
            result['remove_burst_hair_back'] = self.remove_burst_hair_back
        return result

    def from_dict(self, m):
        """
        Populate the model instance from a dictionary.

        Nested dictionaries are recursively converted to model objects.

        :param m: Dictionary containing model data
        :type m: dict

        :return: Self reference for method chaining
        :rtype: PartialHumanOptions

        :raises TypeError: If input is not a dictionary type
        :raises ValueError: If nested model conversion fails
        """
        m = m or dict()
        if m.get('body_smooth_highpass') is not None:
            self.body_smooth_highpass = m.get('body_smooth_highpass')
        if m.get('eye_width_right') is not None:
            self.eye_width_right = m.get('eye_width_right')
        if m.get('skin_red') is not None:
            self.skin_red = m.get('skin_red')
        if m.get('nose_scale') is not None:
            self.nose_scale = m.get('nose_scale')
        if m.get('makeup_eyelash_id') is not None:
            self.makeup_eyelash_id = m.get('makeup_eyelash_id')
        if m.get('remove_eye_streaks') is not None:
            self.remove_eye_streaks = m.get('remove_eye_streaks')
        if m.get('ai_body_flow_thin') is not None:
            self.ai_body_flow_thin = m.get('ai_body_flow_thin')
        if m.get('jaw_width_left') is not None:
            self.jaw_width_left = m.get('jaw_width_left')
        if m.get('cheekbone_width_left') is not None:
            self.cheekbone_width_left = m.get('cheekbone_width_left')
        if m.get('face_color_same') is not None:
            self.face_color_same = m.get('face_color_same')
        if m.get('face_small') is not None:
            self.face_small = m.get('face_small')
        if m.get('remove_forehead_wrinkles') is not None:
            self.remove_forehead_wrinkles = m.get('remove_forehead_wrinkles')
        if m.get('eye_scale_same') is not None:
            self.eye_scale_same = m.get('eye_scale_same')
        if m.get('makeup_shadow') is not None:
            self.makeup_shadow = m.get('makeup_shadow')
        if m.get('makeup_eyebrow') is not None:
            self.makeup_eyebrow = m.get('makeup_eyebrow')
        if m.get('makeup_blush') is not None:
            self.makeup_blush = m.get('makeup_blush')
        if m.get('makeup_lipstick') is not None:
            self.makeup_lipstick = m.get('makeup_lipstick')
        if m.get('leg_thin') is not None:
            self.leg_thin = m.get('leg_thin')
        if m.get('remove_double_chin') is not None:
            self.remove_double_chin = m.get('remove_double_chin')
        if m.get('face_symmetry') is not None:
            self.face_symmetry = m.get('face_symmetry')
        if m.get('eye_height') is not None:
            self.eye_height = m.get('eye_height')
        if m.get('eye_width') is not None:
            self.eye_width = m.get('eye_width')
        if m.get('remove_burst_hair_body') is not None:
            self.remove_burst_hair_body = m.get('remove_burst_hair_body')
        if m.get('face_smooth_new') is not None:
            self.face_smooth_new = m.get('face_smooth_new')
        if m.get('remove_body_flaw') is not None:
            self.remove_body_flaw = m.get('remove_body_flaw')
        if m.get('teeth_white_add_bright') is not None:
            self.teeth_white_add_bright = m.get('teeth_white_add_bright')
        if m.get('neck_thin') is not None:
            self.neck_thin = m.get('neck_thin')
        if m.get('hairline_height') is not None:
            self.hairline_height = m.get('hairline_height')
        if m.get('right_eyebrow_enhance') is not None:
            self.right_eyebrow_enhance = m.get('right_eyebrow_enhance')
        if m.get('remove_face_glossy') is not None:
            self.remove_face_glossy = m.get('remove_face_glossy')
        if m.get('clothes_flaw_remove') is not None:
            self.clothes_flaw_remove = m.get('clothes_flaw_remove')
        if m.get('fill_hair_part') is not None:
            self.fill_hair_part = m.get('fill_hair_part')
        if m.get('makeup_eyeball_id') is not None:
            self.makeup_eyeball_id = m.get('makeup_eyeball_id')
        if m.get('remove_lip_wrinkles') is not None:
            self.remove_lip_wrinkles = m.get('remove_lip_wrinkles')
        if m.get('shiny_eye') is not None:
            self.shiny_eye = m.get('shiny_eye')
        if m.get('makeup_eyebrow_id') is not None:
            self.makeup_eyebrow_id = m.get('makeup_eyebrow_id')
        if m.get('nose_height') is not None:
            self.nose_height = m.get('nose_height')
        if m.get('lip_plump_up') is not None:
            self.lip_plump_up = m.get('lip_plump_up')
        if m.get('face_thin') is not None:
            self.face_thin = m.get('face_thin')
        if m.get('head_small') is not None:
            self.head_small = m.get('head_small')
        if m.get('skin_prefer') is not None:
            self.skin_prefer = m.get('skin_prefer')
        if m.get('remove_white_hair') is not None:
            self.remove_white_hair = m.get('remove_white_hair')
        if m.get('eye_position') is not None:
            self.eye_position = m.get('eye_position')
        if m.get('face_smooth_gray') is not None:
            self.face_smooth_gray = m.get('face_smooth_gray')
        if m.get('skin_white') is not None:
            self.skin_white = m.get('skin_white')
        if m.get('forehead_height') is not None:
            self.forehead_height = m.get('forehead_height')
        if m.get('eye_scale') is not None:
            self.eye_scale = m.get('eye_scale')
        if m.get('eyebrow_distance') is not None:
            self.eyebrow_distance = m.get('eyebrow_distance')
        if m.get('eye_height_left') is not None:
            self.eye_height_left = m.get('eye_height_left')
        if m.get('eye_width_left') is not None:
            self.eye_width_left = m.get('eye_width_left')
        if m.get('remove_dark_circles') is not None:
            self.remove_dark_circles = m.get('remove_dark_circles')
        if m.get('makeup_freckle_id') is not None:
            self.makeup_freckle_id = m.get('makeup_freckle_id')
        if m.get('jaw_width') is not None:
            self.jaw_width = m.get('jaw_width')
        if m.get('cheekbone_width_right') is not None:
            self.cheekbone_width_right = m.get('cheekbone_width_right')
        if m.get('left_eyebrow_enhance') is not None:
            self.left_eyebrow_enhance = m.get('left_eyebrow_enhance')
        if m.get('body_smooth_fine') is not None:
            self.body_smooth_fine = m.get('body_smooth_fine')
        if m.get('body_color_same') is not None:
            self.body_color_same = m.get('body_color_same')
        if m.get('remove_glasses_reflection') is not None:
            self.remove_glasses_reflection = m.get('remove_glasses_reflection')
        if m.get('makeup_highlight') is not None:
            self.makeup_highlight = m.get('makeup_highlight')
        if m.get('remove_polymastia') is not None:
            self.remove_polymastia = m.get('remove_polymastia')
        if m.get('eye_distance_right') is not None:
            self.eye_distance_right = m.get('eye_distance_right')
        if m.get('mouth_scale') is not None:
            self.mouth_scale = m.get('mouth_scale')
        if m.get('mouth_position') is not None:
            self.mouth_position = m.get('mouth_position')
        if m.get('chin_height') is not None:
            self.chin_height = m.get('chin_height')
        if m.get('eye_height_right') is not None:
            self.eye_height_right = m.get('eye_height_right')
        if m.get('makeup_face_id') is not None:
            self.makeup_face_id = m.get('makeup_face_id')
        if m.get('body_smooth') is not None:
            self.body_smooth = m.get('body_smooth')
        if m.get('skin_color') is not None:
            self.skin_color = m.get('skin_color')
        if m.get('face_v') is not None:
            self.face_v = m.get('face_v')
        if m.get('eye_angle_right') is not None:
            self.eye_angle_right = m.get('eye_angle_right')
        if m.get('lip_plump_down') is not None:
            self.lip_plump_down = m.get('lip_plump_down')
        if m.get('face_width') is not None:
            self.face_width = m.get('face_width')
        if m.get('eye_position_left') is not None:
            self.eye_position_left = m.get('eye_position_left')
        if m.get('eye_position_right') is not None:
            self.eye_position_right = m.get('eye_position_right')
        if m.get('neck_length') is not None:
            self.neck_length = m.get('neck_length')
        if m.get('face_shadow') is not None:
            self.face_shadow = m.get('face_shadow')
        if m.get('skin_bright') is not None:
            self.skin_bright = m.get('skin_bright')
        if m.get('skin_color_id') is not None:
            self.skin_color_id = m.get('skin_color_id')
        if m.get('nose_bridge') is not None:
            self.nose_bridge = m.get('nose_bridge')
        if m.get('nose_tip') is not None:
            self.nose_tip = m.get('nose_tip')
        if m.get('left_swan_neck') is not None:
            self.left_swan_neck = m.get('left_swan_neck')
        if m.get('face_smooth_highpass') is not None:
            self.face_smooth_highpass = m.get('face_smooth_highpass')
        if m.get('eye_scale_right') is not None:
            self.eye_scale_right = m.get('eye_scale_right')
        if m.get('remove_face_flaw') is not None:
            self.remove_face_flaw = m.get('remove_face_flaw')
        if m.get('mouth_width') is not None:
            self.mouth_width = m.get('mouth_width')
        if m.get('face_smooth_lowpass') is not None:
            self.face_smooth_lowpass = m.get('face_smooth_lowpass')
        if m.get('remove_burst_hair') is not None:
            self.remove_burst_hair = m.get('remove_burst_hair')
        if m.get('makeup_eye_shadow_id') is not None:
            self.makeup_eye_shadow_id = m.get('makeup_eye_shadow_id')
        if m.get('body_smooth_lowpass') is not None:
            self.body_smooth_lowpass = m.get('body_smooth_lowpass')
        if m.get('eye_angle') is not None:
            self.eye_angle = m.get('eye_angle')
        if m.get('ai_body_thin') is not None:
            self.ai_body_thin = m.get('ai_body_thin')
        if m.get('makeup_eyelash') is not None:
            self.makeup_eyelash = m.get('makeup_eyelash')
        if m.get('makeup_face') is not None:
            self.makeup_face = m.get('makeup_face')
        if m.get('nose_wing') is not None:
            self.nose_wing = m.get('nose_wing')
        if m.get('teeth_white') is not None:
            self.teeth_white = m.get('teeth_white')
        if m.get('body_thin') is not None:
            self.body_thin = m.get('body_thin')
        if m.get('skin_sharpen') is not None:
            self.skin_sharpen = m.get('skin_sharpen')
        if m.get('eye_scale_left') is not None:
            self.eye_scale_left = m.get('eye_scale_left')
        if m.get('remove_neck_wrinkles') is not None:
            self.remove_neck_wrinkles = m.get('remove_neck_wrinkles')
        if m.get('calvaria_height') is not None:
            self.calvaria_height = m.get('calvaria_height')
        if m.get('jaw_width_right') is not None:
            self.jaw_width_right = m.get('jaw_width_right')
        if m.get('waist_thin') is not None:
            self.waist_thin = m.get('waist_thin')
        if m.get('face_highlight') is not None:
            self.face_highlight = m.get('face_highlight')
        if m.get('remove_eye_around_wrinkles') is not None:
            self.remove_eye_around_wrinkles = m.get('remove_eye_around_wrinkles')
        if m.get('eyebrow_thickness') is not None:
            self.eyebrow_thickness = m.get('eyebrow_thickness')
        if m.get('teeth_repair') is not None:
            self.teeth_repair = m.get('teeth_repair')
        if m.get('right_swan_neck') is not None:
            self.right_swan_neck = m.get('right_swan_neck')
        if m.get('arm_thin') is not None:
            self.arm_thin = m.get('arm_thin')
        if m.get('makeup_eyeball') is not None:
            self.makeup_eyeball = m.get('makeup_eyeball')
        if m.get('cheekbone_width') is not None:
            self.cheekbone_width = m.get('cheekbone_width')
        if m.get('eye_angle_left') is not None:
            self.eye_angle_left = m.get('eye_angle_left')
        if m.get('eye_distance_left') is not None:
            self.eye_distance_left = m.get('eye_distance_left')
        if m.get('makeup_eye_shadow') is not None:
            self.makeup_eye_shadow = m.get('makeup_eye_shadow')
        if m.get('teeth_white_des_yellow') is not None:
            self.teeth_white_des_yellow = m.get('teeth_white_des_yellow')
        if m.get('face_smooth_fine') is not None:
            self.face_smooth_fine = m.get('face_smooth_fine')
        if m.get('makeup_freckle') is not None:
            self.makeup_freckle = m.get('makeup_freckle')
        if m.get('makeup_blush_id') is not None:
            self.makeup_blush_id = m.get('makeup_blush_id')
        if m.get('remove_laugh_line') is not None:
            self.remove_laugh_line = m.get('remove_laugh_line')
        if m.get('makeup_lipstick_id') is not None:
            self.makeup_lipstick_id = m.get('makeup_lipstick_id')
        if m.get('face_smooth') is not None:
            self.face_smooth = m.get('face_smooth')
        if m.get('eyebrow_height') is not None:
            self.eyebrow_height = m.get('eyebrow_height')
        if m.get('eye_distance') is not None:
            self.eye_distance = m.get('eye_distance')
        if m.get('remove_face_moles') is not None:
            self.remove_face_moles = m.get('remove_face_moles')
        if m.get('remove_stretch_mark') is not None:
            self.remove_stretch_mark = m.get('remove_stretch_mark')
        if m.get('remove_burst_hair_back') is not None:
            self.remove_burst_hair_back = m.get('remove_burst_hair_back')
        return self
