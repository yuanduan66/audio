{
  "target_defaults": {
    "conditions": [
      ["OS == 'mac'", {
        "defines": [ "WEBRTC_MAC" ],
      }],
      ["OS == 'linux'", {
        "defines": [ "WEBRTC_LINUX" ],
      }],
    ],
  },
  "targets": [{
    "target_name": "aec",
    "type": "<(library)",
    "dependencies": [
      "signal_processing",
      "webrtc_common",
    ],
    "direct_dependent_settings": {
      "include_dirs": [ "." ],
    },
    "include_dirs": [ "." ],
    "sources": [
      "aec/aec_core.c",
      "aec/aec_core_sse2.c",
      "aec/aec_rdft.c",
      "aec/aec_rdft_sse2.c",
      "aec/aec_resampler.c",
      "aec/echo_cancellation.c",
    ],
  }, {
    "target_name": "agc",
    "type": "<(library)",
    "dependencies": [
      "signal_processing",
      "webrtc_common",
    ],
    "direct_dependent_settings": {
      "include_dirs": [ "." ],
    },
    "include_dirs": [ "." ],
    "sources": [
      "agc/analog_agc.c",
      "agc/digital_agc.c",
    ],
  }, {
    "target_name": "ns",
    "type": "<(library)",
    "dependencies": [
      "signal_processing",
      "webrtc_common",
    ],
    "direct_dependent_settings": {
      "include_dirs": [ "." ],
    },
    "include_dirs": [ "." ],
    "sources": [
      "ns/noise_suppression.c",
      "ns/noise_suppression_x.c",
      "ns/ns_core.c",
      "ns/nsx_core.c",
      "ns/nsx_core_c.c",
    ],
    "conditions": [
      ["target_arch == 'mips'", {
        "sources": [
          "ns/nsx_core_mips.c",
        ],
      }],
      ["target_arch == 'arm'", {
        "sources": [
          "ns/nsx_core_neon.c",
          "ns/nsx_core_neon.S",
          "ns/nsx_core_neon_offsets.c",
        ],
      }],
    ],
  }, {
    "target_name": "signal_processing",
    "type": "<(library)",
    "dependencies": [ "webrtc_common" ],
    "direct_dependent_settings": {
      "include_dirs": [ "." ],
    },
    "include_dirs": [ "." ],
    "sources": [
      "signal_processing/auto_corr_to_refl_coef.c",
      "signal_processing/auto_correlation.c",
      "signal_processing/complex_bit_reverse.c",
      "signal_processing/complex_fft.c",
      "signal_processing/copy_set_operations.c",
      "signal_processing/cross_correlation.c",
      "signal_processing/division_operations.c",
      "signal_processing/dot_product_with_scale.c",
      "signal_processing/downsample_fast.c",
      "signal_processing/energy.c",
      "signal_processing/filter_ar.c",
      "signal_processing/filter_ar_fast_q12.c",
      "signal_processing/filter_ma_fast_q12.c",
      "signal_processing/get_hanning_window.c",
      "signal_processing/get_scaling_square.c",
      "signal_processing/ilbc_specific_functions.c",
      "signal_processing/levinson_durbin.c",
      "signal_processing/lpc_to_refl_coef.c",
      "signal_processing/min_max_operations.c",
      "signal_processing/randomization_functions.c",
      "signal_processing/real_fft.c",
      "signal_processing/refl_coef_to_lpc.c",
      "signal_processing/resample.c",
      "signal_processing/resample_48khz.c",
      "signal_processing/resample_by_2.c",
      "signal_processing/resample_by_2_internal.c",
      "signal_processing/resample_fractional.c",
      "signal_processing/spl_init.c",
      "signal_processing/spl_sqrt.c",
      "signal_processing/spl_sqrt_floor.c",
      "signal_processing/spl_version.c",
      "signal_processing/splitting_filter.c",
      "signal_processing/sqrt_of_one_minus_x_squared.c",
      "signal_processing/vector_scaling_operations.c",
    ],
    "conditions": [
      ["target_arch == 'mips'", {
        "sources": [
          "signal_processing/complex_bit_reverse_mips.c",
          "signal_processing/complex_fft_mips.c",
          "signal_processing/cross_correlation_mips.c",
          "signal_processing/downsample_fast_mips.c",
          "signal_processing/filter_ar_fast_q12_mips.c",
          "signal_processing/min_max_operations_mips.c",
          "signal_processing/resample_by_2_mips.c",
          "signal_processing/spl_sqrt_floor_mips.c",
          "signal_processing/vector_scaling_operations_mips.c",
        ],
      }],
      ["target_arch == 'arm'", {
        "sources": [
          "signal_processing/complex_bit_reverse_arm.S",
          "signal_processing/cross_correlation_neon.S",
          "signal_processing/downsample_fast_neon.S",
          "signal_processing/filter_ar_fast_q12_armv7.S",
          "signal_processing/min_max_operations_neon.S",
          "signal_processing/spl_sqrt_floor_arm.S",
          "signal_processing/vector_scaling_operations_neon.S",
        ],
      }],
    ],
  }, {
    "target_name": "webrtc_common",
    "type": "<(library)",
    "direct_dependent_settings": {
      "include_dirs": [ "." ],
    },
    "include_dirs": [ "." ],
    "sources": [
      "webrtc/cpu_features.cc",
      "webrtc/delay_estimator.c",
      "webrtc/delay_estimator_wrapper.c",
      "webrtc/fft4g.c",
      "webrtc/ring_buffer.c",
    ],
  }]
}
