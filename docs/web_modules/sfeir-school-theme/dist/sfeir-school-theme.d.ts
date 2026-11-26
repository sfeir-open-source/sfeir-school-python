import { Reveal as Reveal_2 } from '@talk-control/talk-control-revealjs-extensions';

export { Reveal_2 as Reveal }

export declare const SfeirThemeInitializer: {
    init(params: ((showType?: string) => SlidePath[]) | SfeirThemeInitializerOptions): Promise<void>;
};

declare type SfeirThemeInitializerOptions = {
    slidesFactory: (showType?: string) => SlidePath[];
    knowStyles?: string[];
    plugins?: Reveal.PluginFunction[];
    defaultLang?: string;
    extrasRenderAttr?: string;
};

declare interface SlidePath {
    path: string;
}

export { }
