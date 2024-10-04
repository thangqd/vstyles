import Color from 'color';
import { StyleSpecification } from '@maplibre/maplibre-gl-style-spec';

/** Represents the structure of a vector layer in a TileJSON specification. */
interface VectorLayer {
    id: string;
    fields: Record<string, 'Boolean' | 'Number' | 'String'>;
    description?: string;
    minzoom?: number;
    maxzoom?: number;
}

/** Basic structure for TileJSON specification, applicable to both raster and vector types. */
interface TileJSONSpecificationBasic {
    tilejson: '3.0.0';
    tiles: string[];
    attribution?: string;
    bounds?: [number, number, number, number];
    center?: [number, number];
    data?: string[];
    description?: string;
    fillzoom?: number;
    grids?: string[];
    legend?: string;
    maxzoom?: number;
    minzoom?: number;
    name?: string;
    scheme?: 'tms' | 'xyz';
    template?: string;
}
/** Structure for TileJSON specification of raster type, specifying raster-specific properties. */
interface TileJSONSpecificationRaster extends TileJSONSpecificationBasic {
    type: 'raster';
    format: 'avif' | 'jpg' | 'png' | 'webp';
}
/** Structure for TileJSON specification of vector type, specifying vector-specific properties. */
interface TileJSONSpecificationVector extends TileJSONSpecificationBasic {
    type: 'vector';
    format: 'pbf';
    vector_layers: VectorLayer[];
}

/** Type for Maplibre styles specifically designed for raster sources. */
type MaplibreStyleRaster = Omit<StyleSpecification, 'sources'> & {
    'sources': {
        [_: string]: TileJSONSpecificationRaster;
    };
};
/** Type for Maplibre styles specifically designed for vector sources. */
type MaplibreStyleVector = Omit<StyleSpecification, 'sources'> & {
    'sources': {
        [_: string]: TileJSONSpecificationVector;
    };
};
/** Represents a Maplibre style, which can be either raster or vector. */
type MaplibreStyle = MaplibreStyleRaster | MaplibreStyleVector;

interface RecolorOptions {
    /** If true, inverts the colors. */
    invertBrightness?: boolean;
    /** The degree to rotate the hue of the color (in degrees). */
    rotate?: number;
    /** Adjusts the saturation level of the color. Positive values increase saturation, negative values decrease it. */
    saturate?: number;
    /** Adjusts the gamma of the color. Affects the brightness in a non-linear manner. */
    gamma?: number;
    /** Adjusts the contrast of the color. Higher values produce more contrast. */
    contrast?: number;
    /** Adjusts the brightness of the color. Positive values make it brighter, negative values make it darker. */
    brightness?: number;
    /** Specifies the intensity of the tinting effect. Ranges from 0 (no effect) to 1 (full effect). */
    tint?: number;
    /** Specifies the color used for tinting, in a string format (e.g., '#FF0000'). */
    tintColor?: string;
}

/** Represents language suffixes used in map styles. */
type LanguageSuffix = 'de' | 'en' | undefined;
interface StyleBuilderOptions<T extends StyleBuilder<T>> {
    /** The base URL for loading external resources like tiles, sprites, and fonts. */
    baseUrl?: string;
    /** The URL template for loading font glyphs, formatted with `{fontstack}` and `{range}` placeholders. */
    glyphs?: string;
    /** The URL for loading sprite images and metadata. */
    sprite?: string;
    /** An array of URL templates for loading map tiles, with `{z}`, `{x}`, and `{y}` placeholders. */
    tiles?: string[];
    /** If true, hides all map labels. */
    hideLabels?: boolean;
    /** Suffix to append to language-specific resources, such as `"-en"` for English. */
    languageSuffix?: LanguageSuffix;
    /** An object specifying overrides for default color values, keyed by the color names. */
    colors?: Partial<StyleBuilderColorStrings<T>>;
    /** An object specifying overrides for default font names, keyed by the font names. */
    fonts?: Partial<StyleBuilderFontStrings<T>>;
    /** Options for color adjustments and transformations applied to the entire style. */
    recolor?: RecolorOptions;
}
/** Defines the keys for color properties in a style builder. */
type StyleBuilderColorKeys<T extends StyleBuilder<T>> = keyof T['defaultColors'];
/** Defines the keys for font properties in a style builder. */
type StyleBuilderFontKeys<T extends StyleBuilder<T>> = keyof T['defaultFonts'];
/** Records string values for color properties in a style builder. */
type StyleBuilderColorStrings<T extends StyleBuilder<T>> = Record<StyleBuilderColorKeys<T>, string>;
/** Records string values for font properties in a style builder. */
type StyleBuilderFontStrings<T extends StyleBuilder<T>> = Record<StyleBuilderFontKeys<T>, string>;
/** Records Color objects for color properties in a style builder. */
type StyleBuilderColors<T extends StyleBuilder<T>> = Record<StyleBuilderColorKeys<T>, Color>;
/** Defines options for style rules in a style builder. */
interface StyleRulesOptions<T extends StyleBuilder<T>> {
    colors: StyleBuilderColors<T>;
    fonts: StyleBuilderFontStrings<T>;
    languageSuffix: LanguageSuffix;
}
/** Defines the value type for a style rule. */
type StyleRuleValue = boolean | number | object | string;
/** Defines the structure of a style rule, which is a record of properties to style values. */
type StyleRule = Record<string, StyleRuleValue | undefined>;
/** Defines the structure of style rules, which is a record of selectors to style rules. */
type StyleRules = Record<string, StyleRule | undefined>;

declare abstract class StyleBuilder<Subclass extends StyleBuilder<Subclass>> {
    #private;
    abstract readonly name: string;
    abstract readonly defaultColors: StyleBuilderColorStrings<Subclass>;
    abstract readonly defaultFonts: StyleBuilderFontStrings<Subclass>;
    build(options?: StyleBuilderOptions<Subclass>): MaplibreStyle;
    getColors(colors: StyleBuilderColorStrings<Subclass>): StyleBuilderColors<Subclass>;
    getDefaultOptions(): StyleBuilderOptions<Subclass>;
    protected transformDefaultColors(callback: (color: Color) => Color): void;
    protected abstract getStyleRules(options: StyleRulesOptions<Subclass>): StyleRules;
}

declare class Colorful extends StyleBuilder<Colorful> {
    readonly name: string;
    defaultFonts: {
        regular: string;
        bold: string;
    };
    defaultColors: {
        /** Color for land areas on the map. */
        land: string;
        /** Color for water bodies like lakes and rivers. */
        water: string;
        /** Color for glacier areas, usually shown as white. */
        glacier: string;
        /** Color for wooded or forested areas. */
        wood: string;
        /** Color for grasslands or open fields. */
        grass: string;
        /** Color for parks and recreational areas. */
        park: string;
        /** Color for streets and roads on the map. */
        street: string;
        /** Background color for streets. */
        streetbg: string;
        /** Color for major highways or motorways. */
        motorway: string;
        /** Background color for motorways. */
        motorwaybg: string;
        /** Color for trunk roads. */
        trunk: string;
        /** Background color for trunk roads. */
        trunkbg: string;
        /** Background color for buildings. */
        buildingbg: string;
        /** Primary color for buildings. */
        building: string;
        /** Color used for boundaries. */
        boundary: string;
        /** Color used for disputed boundaries. */
        disputed: string;
        /** Color used for residential areas. */
        residential: string;
        /** Color used for commercial areas. */
        commercial: string;
        /** Color used for industrial areas. */
        industrial: string;
        /** Color used for footpaths and pedestrian areas. */
        foot: string;
        /** Primary color used for labels. */
        label: string;
        /** Color used for label halos. */
        labelHalo: string;
        /** Color used for shields on maps. */
        shield: string;
        /** Color used for agriculture areas. */
        agriculture: string;
        /** Color used for railways. */
        rail: string;
        /** Color used for subways and underground systems. */
        subway: string;
        /** Color used for cycle paths. */
        cycle: string;
        /** Color used for waste areas. */
        waste: string;
        /** Color used for burial and cemetery areas. */
        burial: string;
        /** Color used for sand areas like beaches. */
        sand: string;
        /** Color used for rocky terrain. */
        rock: string;
        /** Color used for leisure areas like parks and gardens. */
        leisure: string;
        /** Color used for wetland areas like marshes. */
        wetland: string;
        /** Color used for various symbols on the map. */
        symbol: string;
        /** Color indicating danger or warning areas. */
        danger: string;
        /** Color used for prison areas. */
        prison: string;
        /** Color used for parking areas. */
        parking: string;
        /** Color used for construction sites. */
        construction: string;
        /** Color used for educational facilities. */
        education: string;
        /** Color used for hospitals and medical facilities. */
        hospital: string;
        /** Color used for points of interest. */
        poi: string;
    };
    protected getStyleRules(options: StyleRulesOptions<Colorful>): StyleRules;
}

declare class Eclipse extends Colorful {
    readonly name: string;
    constructor();
}

declare class Graybeard extends Colorful {
    readonly name: string;
    constructor();
}

declare class Neutrino extends StyleBuilder<Neutrino> {
    readonly name: string;
    defaultFonts: {
        regular: string;
        bold: string;
    };
    defaultColors: {
        /** Color representing land areas. */
        land: string;
        /** Color representing bodies of water such as lakes and rivers. */
        water: string;
        /** Color for grassy areas and fields. */
        grass: string;
        /** Color for wooded or forested areas. */
        wood: string;
        /** Color used for agricultural land. */
        agriculture: string;
        /** Color for site areas such as parks or recreational facilities. */
        site: string;
        /** Primary color for buildings. */
        building: string;
        /** Color for streets and roads. */
        street: string;
        /** Color used for boundaries, such as national or state lines. */
        boundary: string;
        /** Color for footpaths and pedestrian areas. */
        foot: string;
        /** Color used for railways. */
        rail: string;
        /** Primary color used for text labels. */
        label: string;
    };
    protected getStyleRules(options: StyleRulesOptions<Neutrino>): StyleRules;
}

type ColorfulOptions = StyleBuilderOptions<Colorful>;
type EclipseOptions = StyleBuilderOptions<Eclipse>;
type GraybeardOptions = StyleBuilderOptions<Graybeard>;
type NeutrinoOptions = StyleBuilderOptions<Neutrino>;
type SomeOptions = ColorfulOptions | EclipseOptions | GraybeardOptions | NeutrinoOptions;
type MakeStyle<T extends StyleBuilder<T>, O extends StyleBuilderOptions<T>> = ((options?: O) => MaplibreStyle) & {
    getOptions: () => O;
};
type ColorfulBuilder = MakeStyle<Colorful, ColorfulOptions>;
type EclipseBuilder = MakeStyle<Eclipse, EclipseOptions>;
type GraybeardBuilder = MakeStyle<Graybeard, GraybeardOptions>;
type NeutrinoBuilder = MakeStyle<Neutrino, NeutrinoOptions>;
type SomeBuilder = ColorfulBuilder | GraybeardBuilder | NeutrinoBuilder;
declare const colorful: ColorfulBuilder;
declare const eclipse: EclipseBuilder;
declare const graybeard: GraybeardBuilder;
declare const neutrino: NeutrinoBuilder;

type index_d_ColorfulBuilder = ColorfulBuilder;
type index_d_ColorfulOptions = ColorfulOptions;
type index_d_EclipseBuilder = EclipseBuilder;
type index_d_EclipseOptions = EclipseOptions;
type index_d_GraybeardBuilder = GraybeardBuilder;
type index_d_GraybeardOptions = GraybeardOptions;
type index_d_MaplibreStyle = MaplibreStyle;
type index_d_NeutrinoBuilder = NeutrinoBuilder;
type index_d_NeutrinoOptions = NeutrinoOptions;
type index_d_RecolorOptions = RecolorOptions;
type index_d_SomeBuilder = SomeBuilder;
type index_d_SomeOptions = SomeOptions;
declare const index_d_colorful: typeof colorful;
declare const index_d_eclipse: typeof eclipse;
declare const index_d_graybeard: typeof graybeard;
declare const index_d_neutrino: typeof neutrino;
declare namespace index_d {
  export { type index_d_ColorfulBuilder as ColorfulBuilder, type index_d_ColorfulOptions as ColorfulOptions, type index_d_EclipseBuilder as EclipseBuilder, type index_d_EclipseOptions as EclipseOptions, type index_d_GraybeardBuilder as GraybeardBuilder, type index_d_GraybeardOptions as GraybeardOptions, type index_d_MaplibreStyle as MaplibreStyle, type index_d_NeutrinoBuilder as NeutrinoBuilder, type index_d_NeutrinoOptions as NeutrinoOptions, type index_d_RecolorOptions as RecolorOptions, type index_d_SomeBuilder as SomeBuilder, type index_d_SomeOptions as SomeOptions, index_d_colorful as colorful, index_d_eclipse as eclipse, index_d_graybeard as graybeard, index_d_neutrino as neutrino };
}

interface GuessContainerOptions {
    tiles: string[];
    attribution?: string;
    baseUrl?: string;
    bounds?: [number, number, number, number];
    center?: [number, number];
    description?: string;
    fillzoom?: number;
    glyphs?: string;
    grids?: string[];
    legend?: string;
    maxzoom?: number;
    minzoom?: number;
    name?: string;
    scheme?: 'tms' | 'xyz';
    sprite?: string;
    template?: string;
}
/** Options for creating TileJSON, extending the basic specification with format and optional vector layers. */
interface GuessStyleOptions extends GuessContainerOptions {
    format: 'avif' | 'jpg' | 'pbf' | 'png' | 'webp';
    vectorLayers?: unknown[];
}

declare function guessStyle(opt: GuessStyleOptions): MaplibreStyle;

export { type ColorfulBuilder, type ColorfulOptions, type EclipseBuilder, type EclipseOptions, type GraybeardBuilder, type GraybeardOptions, type GuessStyleOptions, type MaplibreStyle, type NeutrinoBuilder, type NeutrinoOptions, type RecolorOptions, type SomeBuilder, type SomeOptions, colorful, eclipse, graybeard, guessStyle, neutrino, index_d as styles };
