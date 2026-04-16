"""
Type stubs for pxr.UsdValidation (OpenUSD 26.03).

Generated and Verified agenticly against the boost::python binding sources at:
  /OpenUSD/pxr/usdValidation/usdValidation/wrap*.cpp
  /OpenUSD/pxr/usdValidation/usdValidation/module.cpp

Each class, method, property, and constructor overload below was confirmed
present in the corresponding wrapXxx.cpp file. Nothing speculative.

Conventions:
- TfToken             -> str  (accepted on input, returned as str)
- TfTokenVector       -> list[str]
- SdfLayerHandle      -> Sdf.Layer
- UsdStagePtr         -> Usd.Stage
- SdfPath             -> Sdf.Path
- UsdPrim             -> Usd.Prim
- UsdPrimRange        -> Usd.PrimRange
- UsdTimeCode         -> Usd.TimeCode
- UsdEditTarget       -> Usd.EditTarget
- GfInterval          -> Gf.Interval
- PlugPluginPtr       -> Plug.Plugin
- VtValue             -> Any
"""

from __future__ import annotations

from typing import Any, ClassVar, overload

import pxr.Tf
from pxr import Gf, Plug, Sdf, Usd

__all__: list[str] = [
    "ValidationContext",
    "ValidationError",
    "ValidationErrorSite",
    "ValidationErrorType",
    "ValidationFixer",
    "ValidationRegistry",
    "ValidationTimeRange",
    "Validator",
    "ValidatorMetadata",
    "ValidatorSuite",
]

__MFB_FULL_PACKAGE_NAME: str = "usdValidation"

# ---------------------------------------------------------------------------
# ValidationErrorType (enum)
# Source: wrapError.cpp:56  —  TfPyWrapEnum<UsdValidationErrorType>(...)
# ---------------------------------------------------------------------------
class ValidationErrorType(pxr.Tf.Tf_PyEnumWrapper):
    """Severity of a validation error."""

    None_: ClassVar[ValidationErrorType]
    Error: ClassVar[ValidationErrorType]
    Warn: ClassVar[ValidationErrorType]
    Info: ClassVar[ValidationErrorType]

    # name and value are inherited from Tf_PyEnumWrapper.

# ---------------------------------------------------------------------------
# ValidationErrorSite
# Source: wrapError.cpp:58-77
# ---------------------------------------------------------------------------
class ValidationErrorSite:
    """Describes the location (layer / stage / prim / property) of a validation error."""

    # wrapError.cpp:59  — init<>()
    @overload
    def __init__(self) -> None: ...
    # wrapError.cpp:60-61  — init<SdfLayerHandle, SdfPath>
    @overload
    def __init__(self, layer: Sdf.Layer, objectPath: Sdf.Path) -> None: ...
    # wrapError.cpp:62-63  — init<UsdStagePtr, SdfPath, SdfLayerHandle>
    #   stage first, objectPath second, optional layer third
    @overload
    def __init__(
        self,
        stage: Usd.Stage,
        objectPath: Sdf.Path,
        layer: Sdf.Layer | None = ...,
    ) -> None: ...
    def IsValid(self) -> bool: ...
    def IsValidSpecInLayer(self) -> bool: ...
    def IsPrim(self) -> bool: ...
    def IsProperty(self) -> bool: ...
    def GetPropertySpec(self) -> Sdf.PropertySpec | None: ...
    def GetPrimSpec(self) -> Sdf.PrimSpec | None: ...
    def GetLayer(self) -> Sdf.Layer | None: ...
    def GetStage(self) -> Usd.Stage | None: ...
    def GetPrim(self) -> Usd.Prim: ...
    def GetProperty(self) -> Usd.Property: ...

    # wrapError.cpp:76-77  — def(self == self) / def(self != self)
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

# ---------------------------------------------------------------------------
# ValidationError
# Source: wrapError.cpp:80-129
# ---------------------------------------------------------------------------
class ValidationError:
    """Entity returned by a validation task; describes a single rule violation."""

    # wrapError.cpp:81  — init<>()
    @overload
    def __init__(self) -> None: ...
    # wrapError.cpp:82-84
    #   init<TfToken, UsdValidationErrorType, UsdValidationErrorSites, string>
    #   Note: no 'data' parameter in the binding — data is set only from C++.
    @overload
    def __init__(
        self,
        name: str,
        errorType: ValidationErrorType,
        errorSites: list[ValidationErrorSite],
        errorMessage: str,
    ) -> None: ...

    # wrapError.cpp:85-89
    def GetName(self) -> str: ...
    # wrapError.cpp:90-91  — raises Tf.ErrorException if no validator attached
    def GetIdentifier(self) -> str: ...
    # wrapError.cpp:92
    def GetType(self) -> ValidationErrorType: ...
    # wrapError.cpp:93-97
    def GetSites(self) -> list[ValidationErrorSite]: ...
    # wrapError.cpp:98-99
    def GetMessage(self) -> str: ...
    # wrapError.cpp:100
    def GetErrorAsString(self) -> str: ...
    # wrapError.cpp:101
    def GetValidator(self) -> Validator: ...
    # wrapError.cpp:102
    def HasNoError(self) -> bool: ...
    # wrapError.cpp:103-107
    def GetData(self) -> Any: ...

    # Fixer access — note different signatures from Validator's fixer methods.
    # wrapError.cpp:108
    def GetFixers(self) -> list[ValidationFixer]: ...
    # wrapError.cpp:109-116  — arg("name")
    def GetFixerByName(self, name: str) -> ValidationFixer | None: ...
    # wrapError.cpp:117  — no args (uses this error's own name)
    def GetFixersByErrorName(self) -> list[ValidationFixer]: ...
    # wrapError.cpp:118-125  — arg("name") only (error name is implied)
    def GetFixerByNameAndErrorName(self, name: str) -> ValidationFixer | None: ...
    # wrapError.cpp:126-127  — arg("keywords")
    def GetFixersByKeywords(self, keywords: list[str]) -> list[ValidationFixer]: ...

    # wrapError.cpp:128-129
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

# ---------------------------------------------------------------------------
# ValidationFixer
# Source: wrapFixer.cpp:25-63
# Note: all accessors are exposed as *properties* via add_property, NOT
#       as Get*() methods.  The class uses no_init.
# ---------------------------------------------------------------------------
class ValidationFixer:
    """A concrete fix that can be applied to a matching ValidationError."""

    # wrapFixer.cpp:26-31  — add_property("name", ...)
    @property
    def name(self) -> str: ...
    # wrapFixer.cpp:32-37  — add_property("description", ...)
    @property
    def description(self) -> str: ...
    # wrapFixer.cpp:38-43  — add_property("errorName", ...)
    @property
    def errorName(self) -> str: ...
    # wrapFixer.cpp:44-49  — add_property("keywords", ...)
    @property
    def keywords(self) -> list[str]: ...

    # wrapFixer.cpp:50-51
    def IsAssociatedWithErrorName(self, errorName: str) -> bool: ...
    # wrapFixer.cpp:52-53
    def HasKeyword(self, keyword: str) -> bool: ...
    # wrapFixer.cpp:54-57  — timeCode defaults to UsdTimeCode::Default()
    def CanApplyFix(
        self,
        error: ValidationError,
        editTarget: Usd.EditTarget,
        timeCode: Usd.TimeCode = ...,
    ) -> bool: ...
    # wrapFixer.cpp:58-61  — timeCode defaults to UsdTimeCode::Default()
    def ApplyFix(
        self,
        error: ValidationError,
        editTarget: Usd.EditTarget,
        timeCode: Usd.TimeCode = ...,
    ) -> bool: ...

# ---------------------------------------------------------------------------
# ValidatorMetadata
# Source: wrapValidator.cpp:101-128
# ---------------------------------------------------------------------------
class ValidatorMetadata:
    """Metadata describing a validator: name, plugin, keywords, doc, schema types, flags."""

    # wrapValidator.cpp:110-112  — add_property("name", ...) read-only
    @property
    def name(self) -> str: ...
    # wrapValidator.cpp:113-115  — add_property("plugin", ...) read-only
    @property
    def plugin(self) -> Plug.Plugin | None: ...
    # wrapValidator.cpp:116  — def_readonly("doc", ...)
    @property
    def doc(self) -> str: ...
    # wrapValidator.cpp:117-118  — def_readonly("isTimeDependent", ...)
    @property
    def isTimeDependent(self) -> bool: ...
    # wrapValidator.cpp:119  — def_readonly("isSuite", ...)
    @property
    def isSuite(self) -> bool: ...

    # wrapValidator.cpp:102-109  — make_constructor with keyword defaults
    def __init__(
        self,
        name: str = ...,
        plugin: Plug.Plugin | None = ...,
        keywords: list[str] = ...,
        doc: str = ...,
        schemaTypes: list[str] = ...,
        isTimeDependent: bool = ...,
        isSuite: bool = ...,
    ) -> None: ...

    # wrapValidator.cpp:120-123
    def GetKeywords(self) -> list[str]: ...
    # wrapValidator.cpp:124-127
    def GetSchemaTypes(self) -> list[str]: ...

# ---------------------------------------------------------------------------
# Validator
# Source: wrapValidator.cpp:131-193
# Not constructible from Python (no_init).
# ---------------------------------------------------------------------------
class Validator:
    """A single validation test. Retrieved from ValidationRegistry, not constructed directly."""

    # wrapValidator.cpp:132-136
    def GetMetadata(self) -> ValidatorMetadata: ...

    # --- Validate overloads ---
    # wrapValidator.cpp:137-144  — Validate(layer)
    @overload
    def Validate(self, layer: Sdf.Layer) -> list[ValidationError]: ...
    # wrapValidator.cpp:145-154  — Validate(stage, timeRange=default)
    @overload
    def Validate(
        self,
        stage: Usd.Stage,
        timeRange: ValidationTimeRange = ...,
    ) -> list[ValidationError]: ...
    # wrapValidator.cpp:155-163  — Validate(prim, timeRange=default)
    @overload
    def Validate(
        self,
        prim: Usd.Prim,
        timeRange: ValidationTimeRange = ...,
    ) -> list[ValidationError]: ...

    # --- Fixer access ---
    # wrapValidator.cpp:164
    def GetFixers(self) -> list[ValidationFixer]: ...
    # wrapValidator.cpp:165-172  — arg("name")
    def GetFixerByName(self, name: str) -> ValidationFixer | None: ...
    # wrapValidator.cpp:173-174  — arg("errorName")
    def GetFixersByErrorName(self, errorName: str) -> list[ValidationFixer]: ...
    # wrapValidator.cpp:175-184  — arg("name"), arg("errorName")
    def GetFixerByNameAndErrorName(
        self, name: str, errorName: str
    ) -> ValidationFixer | None: ...
    # wrapValidator.cpp:185-186  — arg("keywords")
    def GetFixersByKeywords(self, keywords: list[str]) -> list[ValidationFixer]: ...

    # wrapValidator.cpp:187-191  — pointer equality only
    def __eq__(self, other: object) -> bool: ...
    # wrapValidator.cpp:192
    def __repr__(self) -> str: ...

# ---------------------------------------------------------------------------
# ValidatorSuite
# Source: wrapValidator.cpp:195-207
# Not constructible from Python (no_init).
# ---------------------------------------------------------------------------
class ValidatorSuite:
    """A named collection of validators run together."""

    # wrapValidator.cpp:196-200
    def GetMetadata(self) -> ValidatorMetadata: ...
    # wrapValidator.cpp:201
    def GetContainedValidators(self) -> list[Validator]: ...

    # wrapValidator.cpp:202-205  — pointer equality only
    def __eq__(self, other: object) -> bool: ...

# ---------------------------------------------------------------------------
# ValidationTimeRange
# Source: wrapTimeRange.cpp:24-31
# ---------------------------------------------------------------------------
class ValidationTimeRange:
    """Interval (plus optional default-time flag) over which validation runs."""

    # wrapTimeRange.cpp:24  — default ctor
    @overload
    def __init__(self) -> None: ...
    # wrapTimeRange.cpp:25-26  — init<UsdTimeCode>
    @overload
    def __init__(self, timeCode: Usd.TimeCode) -> None: ...
    # wrapTimeRange.cpp:27-28  — init<GfInterval, bool>
    #   includeTimeCodeDefault defaults to false
    @overload
    def __init__(
        self, interval: Gf.Interval, includeTimeCodeDefault: bool = ...
    ) -> None: ...

    # wrapTimeRange.cpp:29-30
    def IncludesTimeCodeDefault(self) -> bool: ...
    # wrapTimeRange.cpp:31
    def GetInterval(self) -> Gf.Interval: ...

# ---------------------------------------------------------------------------
# ValidationRegistry (singleton)
# Source: wrapRegistry.cpp:100-148
#
# IMPORTANT: No registration methods (RegisterValidator, RegisterPlugin-
# Validator, RegisterPluginValidatorSuite, RegisterValidatorSuite) are
# exposed in the Python bindings. Registration is C++ only.
# ---------------------------------------------------------------------------
class ValidationRegistry:
    """Registry of all known validators and validator suites. Singleton."""

    # wrapRegistry.cpp:104-107  — singleton pattern
    def __new__(cls) -> ValidationRegistry: ...
    def __init__(self) -> None: ...

    # --- Existence checks ---
    # wrapRegistry.cpp:108-109
    def HasValidator(self, validatorName: str) -> bool: ...
    # wrapRegistry.cpp:110-111
    def HasValidatorSuite(self, suiteName: str) -> bool: ...

    # --- Validator access ---
    # wrapRegistry.cpp:112
    def GetOrLoadAllValidators(self) -> list[Validator]: ...
    # wrapRegistry.cpp:113-116
    def GetOrLoadValidatorByName(self, validatorName: str) -> Validator | None: ...
    # wrapRegistry.cpp:117-118
    def GetOrLoadValidatorsByName(
        self, validatorNames: list[str]
    ) -> list[Validator]: ...

    # --- Suite access ---
    # wrapRegistry.cpp:119
    def GetOrLoadAllValidatorSuites(self) -> list[ValidatorSuite]: ...
    # wrapRegistry.cpp:120-123
    def GetOrLoadValidatorSuiteByName(
        self, suiteName: str
    ) -> ValidatorSuite | None: ...
    # wrapRegistry.cpp:124-125
    def GetOrLoadValidatorSuitesByName(
        self, suiteNames: list[str]
    ) -> list[ValidatorSuite]: ...

    # --- Metadata queries ---
    # wrapRegistry.cpp:126
    def GetValidatorMetadata(self, name: str) -> ValidatorMetadata | None: ...
    # wrapRegistry.cpp:127-129
    def GetAllValidatorMetadata(self) -> list[ValidatorMetadata]: ...
    # wrapRegistry.cpp:130-132
    def GetValidatorMetadataForPlugin(
        self, pluginName: str
    ) -> list[ValidatorMetadata]: ...
    # wrapRegistry.cpp:133-135
    def GetValidatorMetadataForKeyword(
        self, keyword: str
    ) -> list[ValidatorMetadata]: ...
    # wrapRegistry.cpp:136-138
    def GetValidatorMetadataForSchemaType(
        self, schemaType: str
    ) -> list[ValidatorMetadata]: ...
    # wrapRegistry.cpp:139-141
    def GetValidatorMetadataForPlugins(
        self, pluginNames: list[str]
    ) -> list[ValidatorMetadata]: ...
    # wrapRegistry.cpp:142-144
    def GetValidatorMetadataForKeywords(
        self, keywords: list[str]
    ) -> list[ValidatorMetadata]: ...
    # wrapRegistry.cpp:145-147
    def GetValidatorMetadataForSchemaTypes(
        self, schemaTypes: list[str]
    ) -> list[ValidatorMetadata]: ...

# ---------------------------------------------------------------------------
# ValidationContext
# Source: wrapContext.cpp:32-139
# ---------------------------------------------------------------------------
class ValidationContext:
    """Runs a configured set of validators over layers / stages / prims."""

    # --- Constructor overloads ---
    # wrapContext.cpp:36-37
    @overload
    def __init__(
        self, keywords: list[str], includeAllAncestors: bool = ...
    ) -> None: ...
    # wrapContext.cpp:38-39
    @overload
    def __init__(
        self, plugins: list[Plug.Plugin], includeAllAncestors: bool = ...
    ) -> None: ...
    # wrapContext.cpp:40-41
    @overload
    def __init__(
        self,
        metadata: list[ValidatorMetadata],
        includeAllAncestors: bool = ...,
    ) -> None: ...
    # wrapContext.cpp:42
    @overload
    def __init__(self, schemaTypes: list[pxr.Tf.Type]) -> None: ...
    # wrapContext.cpp:43-44
    @overload
    def __init__(self, validators: list[Validator]) -> None: ...
    # wrapContext.cpp:45-46
    @overload
    def __init__(self, suites: list[ValidatorSuite]) -> None: ...

    # --- Validate overloads ---
    # wrapContext.cpp:47-53  — Validate(layer)
    @overload
    def Validate(self, layer: Sdf.Layer) -> list[ValidationError]: ...
    # wrapContext.cpp:54-60  — Validate(stage)
    @overload
    def Validate(self, stage: Usd.Stage) -> list[ValidationError]: ...
    # wrapContext.cpp:61-68  — Validate(stage, predicate)
    @overload
    def Validate(
        self, stage: Usd.Stage, predicate: Usd._PrimFlagsPredicate
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:69-77  — Validate(stage, predicate, timeRange)
    @overload
    def Validate(
        self,
        stage: Usd.Stage,
        predicate: Usd._PrimFlagsPredicate,
        timeRange: ValidationTimeRange,
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:78-85  — Validate(stage, timeRange)
    @overload
    def Validate(
        self, stage: Usd.Stage, timeRange: ValidationTimeRange
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:86-94  — Validate(stage, predicate, timeCodes)
    @overload
    def Validate(
        self,
        stage: Usd.Stage,
        predicate: Usd._PrimFlagsPredicate,
        timeCodes: list[Usd.TimeCode],
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:95-102  — Validate(stage, timeCodes)
    @overload
    def Validate(
        self, stage: Usd.Stage, timeCodes: list[Usd.TimeCode]
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:103-112  — Validate(list[Prim], timeRange=default)
    @overload
    def Validate(
        self, prims: list[Usd.Prim], timeRange: ValidationTimeRange = ...
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:113-121  — Validate(PrimRange, timeRange=default)
    @overload
    def Validate(
        self, prims: Usd.PrimRange, timeRange: ValidationTimeRange = ...
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:122-130  — Validate(list[Prim], timeCodes)
    @overload
    def Validate(
        self, prims: list[Usd.Prim], timeCodes: list[Usd.TimeCode]
    ) -> list[ValidationError]: ...
    # wrapContext.cpp:131-138  — Validate(PrimRange, timeCodes)
    @overload
    def Validate(
        self, prims: Usd.PrimRange, timeCodes: list[Usd.TimeCode]
    ) -> list[ValidationError]: ...
