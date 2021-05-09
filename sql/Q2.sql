select habitat_id, cap_color_id, count(*) as count 
from mushrooms
group by habitat_id, cap_color_id
