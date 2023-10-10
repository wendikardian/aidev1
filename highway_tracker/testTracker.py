import math

class EuclideanDistTracker:
    def __init__(self):
        self.center_points = {}
        self.id_count = 0

    def update(self, object_rect):
        object_bbs_ids = []
        for rect in object_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2
            # print(cx, cy)
            same_object_detected = False
            for id, pt in self.center_points.items():
                dist = math.hypot(cx - pt[0], cy - pt[1])
                if dist < 50:
                    self.center_points[id] = (cx, cy)
                    object_bbs_ids.append([x, y, w, h, id])
                    same_object_detected = True
                    break

            if same_object_detected == False:
                self.center_points[self.id_count] = (cx, cy)
                object_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1
                print(self.center_points)

        new_center_points = {}
        for object_id in object_bbs_ids:
            Nx, Ny, Nw, Nh, id = object_id
            center = self.center_points[id]
            new_center_points[id] = center
        self.center_points = new_center_points.copy()
        return object_bbs_ids