# QGIS DevTools Plugin
# Copyright (C) 2025  NextGIS
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or any
# later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <https://www.gnu.org/licenses/>.


from typing import TYPE_CHECKING, Any, Dict, List, Set

from qgis.core import (
    Qgis,
    QgsFeature,
    QgsFeatureRequest,
    QgsGeometry,
    QgsMapLayerProxyModel,
    QgsMapLayerType,
    QgsWkbTypes,
)
from qgis.PyQt.QtCore import QMetaType, QVariant

QGIS_3_30 = 33000
QGIS_3_32 = 33200
QGIS_3_34 = 33400
QGIS_3_36 = 33600
QGIS_3_38 = 33800
QGIS_3_40 = 34000
QGIS_3_42 = 34200
QGIS_3_42_2 = 34202


QgsFeatureId = int
QgsFeatureIds = Set[QgsFeatureId]
QgsFeatureList = List[QgsFeature]

QgsAttributeList = List[int]
QgsAttributeMap = Dict[int, Any]
QgsChangedAttributesMap = Dict[
    QgsFeatureId, Dict[QgsFeatureId, QgsAttributeMap]
]

QgsGeometryMap = Dict[QgsFeatureId, QgsGeometry]


if Qgis.versionInt() >= QGIS_3_30 or TYPE_CHECKING:
    WkbType = Qgis.WkbType

    GeometryType = Qgis.GeometryType

    LayerType = Qgis.LayerType

else:
    WkbType = QgsWkbTypes.Type

    GeometryType = QgsWkbTypes.GeometryType
    GeometryType.Point = GeometryType.PointGeometry
    GeometryType.Point.is_monkey_patched = True
    GeometryType.Line = GeometryType.LineGeometry
    GeometryType.Line.is_monkey_patched = True
    GeometryType.Polygon = GeometryType.PolygonGeometry
    GeometryType.Polygon.is_monkey_patched = True
    GeometryType.Unknown = GeometryType.UnknownGeometry
    GeometryType.Unknown.is_monkey_patched = True
    GeometryType.Null = GeometryType.NullGeometry
    GeometryType.Null.is_monkey_patched = True

    LayerType = QgsMapLayerType
    LayerType.Vector = QgsMapLayerType.VectorLayer
    LayerType.Vector.is_monkey_patched = True
    LayerType.Raster = QgsMapLayerType.RasterLayer
    LayerType.Raster.is_monkey_patched = True
    LayerType.Plugin = QgsMapLayerType.PluginLayer
    LayerType.Plugin.is_monkey_patched = True
    LayerType.Mesh = QgsMapLayerType.MeshLayer
    LayerType.Mesh.is_monkey_patched = True
    LayerType.VectorTile = QgsMapLayerType.VectorTileLayer
    LayerType.VectorTile.is_monkey_patched = True
    LayerType.Annotation = QgsMapLayerType.AnnotationLayer
    LayerType.Annotation.is_monkey_patched = True
    LayerType.PointCloud = QgsMapLayerType.PointCloudLayer
    LayerType.PointCloud.is_monkey_patched = True

if Qgis.versionInt() >= QGIS_3_34 or TYPE_CHECKING:
    LayerFilter = Qgis.LayerFilter
    LayerFilters = Qgis.LayerFilters

else:
    LayerFilter = QgsMapLayerProxyModel.Filter
    LayerFilters = QgsMapLayerProxyModel.Filters

if Qgis.versionInt() >= QGIS_3_36 or TYPE_CHECKING:
    FeatureRequestFlag = Qgis.FeatureRequestFlag
    FeatureRequestFlags = Qgis.FeatureRequestFlags

else:
    FeatureRequestFlag = QgsFeatureRequest.Flag
    FeatureRequestFlags = QgsFeatureRequest.Flags


if Qgis.versionInt() >= QGIS_3_38 or TYPE_CHECKING:
    FieldType = QMetaType.Type
else:
    FieldType = QVariant.Type
    FieldType.QString = QVariant.Type.String
    FieldType.QString.is_monkey_patched = True
    FieldType.QDate = QVariant.Type.Date
    FieldType.QDate.is_monkey_patched = True
    FieldType.QTime = QVariant.Type.Time
    FieldType.QTime.is_monkey_patched = True
    FieldType.QDateTime = QVariant.Type.DateTime
    FieldType.QDateTime.is_monkey_patched = True

try:
    from packaging import version

    parse_version = version.parse

except Exception:
    import pkg_resources

    parse_version = pkg_resources.parse_version
