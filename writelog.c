/* ----------------------------------------------------------------------
 *
 * Invoke the coNCePTuaL run-time library to generate a dataless log
 * file (but with a complete prologue and epilogue)
 *
 * By Scott Pakin <pakin@lanl.gov>
 *
 * ----------------------------------------------------------------------
 *
 * 
 * Copyright (C) 2003, Triad National Security, LLC
 * All rights reserved.
 * 
 * Copyright (2003).  Triad National Security, LLC.  This software
 * was produced under U.S. Government contract 89233218CNA000001 for
 * Los Alamos National Laboratory (LANL), which is operated by Los
 * Alamos National Security, LLC (Triad) for the U.S. Department
 * of Energy. The U.S. Government has rights to use, reproduce,
 * and distribute this software.  NEITHER THE GOVERNMENT NOR TRIAD
 * MAKES ANY WARRANTY, EXPRESS OR IMPLIED, OR ASSUMES ANY LIABILITY
 * FOR THE USE OF THIS SOFTWARE. If software is modified to produce
 * derivative works, such modified software should be clearly marked,
 * so as not to confuse it with the version available from LANL.
 * 
 * Additionally, redistribution and use in source and binary forms,
 * with or without modification, are permitted provided that the
 * following conditions are met:
 * 
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 * 
 *   * Redistributions in binary form must reproduce the above copyright
 *     notice, this list of conditions and the following disclaimer
 *     in the documentation and/or other materials provided with the
 *     distribution.
 * 
 *   * Neither the name of Triad National Security, LLC, Los Alamos
 *     National Laboratory, the U.S. Government, nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY TRIAD AND CONTRIBUTORS "AS IS" AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL TRIAD OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY,
 * OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT
 * OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
 * BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
 * OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 * 
 *
 * ----------------------------------------------------------------------
 */

#include <stdio.h>
#include <ncptl.h>     /* We expect to be built from the source directory. */

int
main (int argc, char *argv[])
{
  NCPTL_LOG_FILE_STATE *logstate;
  char *log_uuid;

  if (argc < 2) {
    fprintf (stderr, "Usage: %s <template>\n", argv[0]);
    exit (EXIT_FAILURE);
  }
  ncptl_init (NCPTL_RUN_TIME_VERSION, argv[0]);
  logstate = ncptl_log_open (argv[1], 0);
  log_uuid = ncptl_log_generate_uuid();
  ncptl_log_write_prologue (logstate, argv[0], log_uuid, "N/A", "N/A", 1, NULL, 0, NULL);
  ncptl_free (log_uuid);
  ncptl_log_write_epilogue (logstate);
  ncptl_log_close (logstate);
  return 0;
}
