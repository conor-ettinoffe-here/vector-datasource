from . import FixtureTest


# Adds tests for OSM features (but not NE features)
class SortKeyBoundary(FixtureTest):

    def test_usa_country_boundary(self):
        # country boundary of USA
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/148838',
        ], clip=self.tile_bbox(8, 39, 95, padding=0.1))
        self.assert_has_feature(
            8, 39, 95, "boundaries",
            {"kind": "country", "sort_rank": 262})

    def test_nevada_california_boundary(self):
        # region boundary between Nevada - California
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/165473',
            'https://www.openstreetmap.org/relation/165475',
        ], clip=self.tile_bbox(8, 42, 96, padding=0.1))
        self.assert_has_feature(
            8, 42, 96, "boundaries",
            {"kind": "region", "sort_rank": 256})

    def test_mendocino_humboldt_county_boundary(self):
        # county boundary between Mendocino County - Humboldt County
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/396458',
            'https://www.openstreetmap.org/relation/396489',
        ], clip=self.tile_bbox(10, 159, 387, padding=0.1))
        self.assert_has_feature(
            10, 159, 387, "boundaries",
            {"kind": "county", "sort_rank": 254})

    def test_san_francisco_daly_city_locality_boundary(self):
        # locality boundary between San Francisco - Daly City
        self.load_fixtures([
            'https://www.openstreetmap.org/relation/111968',
            'https://www.openstreetmap.org/relation/112271',
        ], clip=self.tile_bbox(10, 163, 396, padding=0.1))
        self.assert_has_feature(
            11, 326, 792, "boundaries",
            {"kind": "locality", "sort_rank": 252})
