from typing import Any, List, Union

from statham.schema.constants import Maybe
from statham.schema.elements import (
    AllOf,
    AnyOf,
    Array,
    Element,
    Integer,
    Number,
    Object,
    OneOf,
    String,
)
from statham.schema.property import Property


class LngString(Object, patternProperties={'^[a-zA-Z-][a-zA-Z-]*$': Array(String()), '^none$': Array(String())}, additionalProperties=False):

    pass


class LODClass(Object):

    id: str = Property(String(format='uri', pattern='^http.*$'), required=True)

    type: str = Property(String(), required=True)

    label: Maybe[LngString] = Property(LngString)


class KeyValueStr(Object):

    label: LngString = Property(LngString, required=True)

    value: LngString = Property(LngString, required=True)


class External(Object):

    format: Maybe[str] = Property(String(pattern='^[a-z][a-z]*/.*$'))

    profile: Maybe[str] = Property(String())


class Service3(Object):

    profile: Maybe[str] = Property(String())


class Service2(Object):

    commercial_at_id: str = Property(String(format='uri', pattern='^http.*$'), required=True, source='@id')

    commercial_at_type: str = Property(String(), required=True, source='@type')

    profile: Maybe[str] = Property(String())


class ImgResource(Object):

    id: str = Property(String(format='uri', pattern='^http.*$'), required=True)

    type: str = Property(String(), required=True)

    height: Maybe[int] = Property(Integer())

    width: Maybe[int] = Property(Integer())

    duration: Maybe[float] = Property(Number(minimum=0))

    language: Maybe[str] = Property(String())

    service: Maybe[List[Union[LODClass, Service2]]] = Property(Array(OneOf(AllOf(LODClass, Service3), Service2)))

    format: Maybe[str] = Property(String(pattern='^[a-z][a-z]*/.*$'))

    label: Maybe[LngString] = Property(LngString)


class TextResource(Object):

    id: Maybe[str] = Property(String(format='uri', pattern='^http.*$'))

    type: str = Property(String(pattern='^TextualBody$'), required=True)

    value: str = Property(String(), required=True)

    format: Maybe[str] = Property(String(pattern='^[a-z][a-z]*/.*$'))

    language: Maybe[str] = Property(String())


class Homepage(Object):

    format: Maybe[str] = Property(String(pattern='^[a-z][a-z]*/.*$'))

    language: Maybe[List[str]] = Property(Array(AnyOf(String(pattern='^[a-zA-Z-][a-zA-Z-]*$'), String(pattern='^none$'))))


class Provider(Object):

    type: Maybe[str] = Property(String(pattern='^Agent$'))

    homepage: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Homepage)))

    logo: Maybe[List[Union[ImgResource, TextResource]]] = Property(Array(OneOf(ImgResource, TextResource)))

    seeAlso: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, External)))


class Choice(Object):

    pass


class Choice_1(Object):

    type: str = Property(String(const='Choice'), required=True)

    items: List[Any] = Property(Array(Element()), required=True)


class Body2Item(Object):

    pass


class DurationSelector(Object):

    type: str = Property(String(), required=True)

    t: Maybe[float] = Property(Number(minimum=0))


class SpecificResource(Object):

    id: Maybe[str] = Property(String(format='uri', pattern='^http.*$'))

    type: Maybe[str] = Property(String(pattern='^SpecificResource$'))

    format: Maybe[str] = Property(String(pattern='^[a-z][a-z]*/.*$'))

    accessibility: Maybe[str] = Property(String())

    source: str = Property(String(format='uri', pattern='^http.*$'), required=True)

    selector: Union[str, DurationSelector] = Property(OneOf(String(format='uri', pattern='^http.*$'), DurationSelector), required=True)


class Annotation(Object):

    type: str = Property(String(pattern='^Annotation$'), required=True)

    motivation: Maybe[Union[str, List[str]]] = Property(OneOf(String(), Array(String())))

    body: Maybe[Union[Union[ImgResource, TextResource], Choice, List[Body2Item]]] = Property(AnyOf(OneOf(ImgResource, TextResource), AllOf(Choice, Choice_1, Element(required=['items'], properties={'items': Property(Array(OneOf(ImgResource, TextResource)), required=True)})), Array(Body2Item)))

    target: Union[Union[str, SpecificResource], List[Union[str, SpecificResource]]] = Property(AnyOf(OneOf(String(format='uri', pattern='^http.*$'), SpecificResource), Array(OneOf(String(format='uri', pattern='^http.*$'), SpecificResource))), required=True)


class AnnotationPage(Object, additionalProperties=False):

    id: Maybe[str] = Property(String(format='uri', pattern='^http.*$'))

    commercial_at_context: Maybe[Any] = Property(Element(), source='@context')

    type: Maybe[str] = Property(String(pattern='^AnnotationPage$'))

    items: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Annotation)))


class Canvas(Object, dependencies={'width': ['height'], 'height': ['width']}):

    type: Maybe[str] = Property(String(pattern='^Canvas$'))

    height: Maybe[int] = Property(Integer())

    width: Maybe[int] = Property(Integer())

    duration: Maybe[float] = Property(Number(minimum=0))

    metadata: Maybe[List[KeyValueStr]] = Property(Array(KeyValueStr))

    summary: Maybe[LngString] = Property(LngString)

    requiredStatement: Maybe[KeyValueStr] = Property(KeyValueStr)

    rights: Maybe[str] = Property(OneOf(String(format='uri', pattern='http://creativecommons.org/licenses/.*'), String(format='uri', pattern='http://creativecommons.org/publicdomain/mark/.*'), String(format='uri', pattern='http://rightsstatements.org/vocab/.*')))

    navDate: Maybe[str] = Property(String(format='date-time'))

    provider: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Provider)))

    seeAlso: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, External)))

    thumbnail: Maybe[List[Union[ImgResource, TextResource]]] = Property(Array(OneOf(ImgResource, TextResource)))

    homepage: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Homepage)))

    behavior: Maybe[List[str]] = Property(Array(AnyOf(String(pattern='^auto-advance$'), String(pattern='^no-auto-advance$'), String(pattern='^repeat$'), String(pattern='^no-repeat$'), String(pattern='^unordered$'), String(pattern='^individuals$'), String(pattern='^continuous$'), String(pattern='^paged$'), String(pattern='^facing-pages$'), String(pattern='^non-paged$'), String(pattern='^multi-part$'), String(pattern='^together$'), String(pattern='^sequence$'), String(pattern='^thumbnail-nav$'), String(pattern='^no-nav$'), String(pattern='^hidden$'))))

    partOf: Maybe[List[LODClass]] = Property(Array(LODClass))

    items: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, AnnotationPage)))

    annotations: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, AnnotationPage)))


class AnnotationCollection(Object):

    type: Maybe[str] = Property(String(pattern='^AnnotationCollection$'))

    partOf: Maybe[List[LODClass]] = Property(Array(LODClass))

    next: Maybe[LODClass] = Property(AllOf(LODClass, AnnotationPage))

    first: Maybe[LODClass] = Property(AllOf(LODClass, AnnotationPage))

    last: Maybe[LODClass] = Property(AllOf(LODClass, AnnotationPage))

    items: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Annotation)))


class RangeCanvas(Object):

    type: Maybe[str] = Property(String(pattern='^Canvas$'))


class Range(Object):

    type: Maybe[str] = Property(String(pattern='^Range$'))

    supplementary: Maybe[LODClass] = Property(AllOf(LODClass, AnnotationCollection))

    items: Maybe[List[Union[SpecificResource, LODClass]]] = Property(Array(OneOf(SpecificResource, AllOf(LODClass, RangeCanvas))))


class Manifest(Object, additionalProperties=False):

    commercial_at_context: Maybe[Union[List[str], str]] = Property(OneOf(Array(String(format='uri', pattern='^http.*$')), String(const='http://iiif.io/api/presentation/3/context.json')), source='@context')

    id: Maybe[Any] = Property(Element())

    label: Maybe[Any] = Property(Element())

    type: Maybe[str] = Property(String(pattern='^Manifest'))

    metadata: Maybe[List[KeyValueStr]] = Property(Array(KeyValueStr))

    summary: Maybe[LngString] = Property(LngString)

    requiredStatement: Maybe[KeyValueStr] = Property(KeyValueStr)

    rendering: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, External)))

    service: Maybe[List[Union[LODClass, Service2]]] = Property(Array(OneOf(AllOf(LODClass, Service3), Service2)))

    viewingDirection: Maybe[str] = Property(AnyOf(String(pattern='^left-to-right$'), String(pattern='^right-to-left$'), String(pattern='^top-to-bottom$'), String(pattern='^bottom-to-top$')))

    rights: Maybe[str] = Property(OneOf(String(format='uri', pattern='http://creativecommons.org/licenses/.*'), String(format='uri', pattern='http://creativecommons.org/publicdomain/mark/.*'), String(format='uri', pattern='http://rightsstatements.org/vocab/.*')))

    start: Maybe[Any] = Property(Element())

    logo: Maybe[List[Union[ImgResource, TextResource]]] = Property(Array(OneOf(ImgResource, TextResource)))

    navDate: Maybe[str] = Property(String(format='date-time'))

    provider: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Provider)))

    seeAlso: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, External)))

    thumbnail: Maybe[List[Union[ImgResource, TextResource]]] = Property(Array(OneOf(ImgResource, TextResource)))

    homepage: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Homepage)))

    behavior: Maybe[List[str]] = Property(Array(AnyOf(String(pattern='^auto-advance$'), String(pattern='^no-auto-advance$'), String(pattern='^repeat$'), String(pattern='^no-repeat$'), String(pattern='^unordered$'), String(pattern='^individuals$'), String(pattern='^continuous$'), String(pattern='^paged$'), String(pattern='^facing-pages$'), String(pattern='^non-paged$'), String(pattern='^multi-part$'), String(pattern='^together$'), String(pattern='^sequence$'), String(pattern='^thumbnail-nav$'), String(pattern='^no-nav$'), String(pattern='^hidden$'))))

    partOf: Maybe[List[LODClass]] = Property(Array(LODClass))

    items: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, AllOf(Canvas, AnyOf(Element(required=['width']), Element(required=['height']), Element(required=['duration']))))))

    structures: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, Range)))

    annotations: Maybe[List[LODClass]] = Property(Array(AllOf(LODClass, AnnotationPage)))
