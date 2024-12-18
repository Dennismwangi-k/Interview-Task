from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ClosestPoints
from .serializers import ClosestPointsSerializer
import math


def determine_closest_pair_distance(points):
    minimum_distance = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
            if dist < minimum_distance:
                minimum_distance = dist
                closest_pair = (points[i], points[j])
    return closest_pair


class ClosestPointsView(APIView):
    def post(self, request):
        points_string = request.data.get('points_string', '')

        if not points_string.strip():
            return Response({"error": "we cannot have empty string "}, status=status.HTTP_400_BAD_REQUEST)

        try:
            points = [tuple(map(int, point.strip("()").split(','))) for point in points_string.split(", ")]

            if len(points) < 2:
                return Response({"error": "For us to calculate the closest pair, we need at least 2 points."},
                                status=status.HTTP_400_BAD_REQUEST)

            closest_pair = determine_closest_pair_distance(points)
            closest_pair_str = f"{closest_pair[0]} and {closest_pair[1]}"

            closest_points = ClosestPoints.objects.create(
                points_string=points_string,
                closest_pair=closest_pair_str
            )

            serializer = ClosestPointsSerializer(closest_points)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError:
            return Response({"error": "The format of 'points_string' is invalid."},
                            status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        points = ClosestPoints.objects.all()
        serializer = ClosestPointsSerializer(points, many=True)
        return Response(serializer.data)
